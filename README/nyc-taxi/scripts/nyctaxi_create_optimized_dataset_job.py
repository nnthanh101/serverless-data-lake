# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import sys

#AWS Glue imports
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

# Spark imports
from pyspark.context import SparkContext
from pyspark.sql.functions import *

### Job initialization boilerplate

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'your_bucket_name'])
your_bucket_name = args['your_bucket_name']

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

### Your ETL Code

# Read our primary Yellow taxi table from raw dataset. This is the biggest table of all with millions of rows.
yellow_dyf = glueContext.create_dynamic_frame.from_catalog(database="nyctaxi", table_name="yellow", transformation_ctx="nyctaxi_yellow_rpt")

# Read the three other look-up tables
taxi_zone_dyf = glueContext.create_dynamic_frame.from_catalog(database="nyctaxi", table_name="taxizone")

payment_type_dyf = glueContext.create_dynamic_frame.from_catalog(database="nyctaxi", table_name="paymenttype")

rate_code_dyf = glueContext.create_dynamic_frame.from_catalog(database="nyctaxi", table_name="ratecode")

# Convert into Spark DataFrames
yellow_df = yellow_dyf.toDF()

# Repartition Yellow into 4 * 4 partitions and cache in-memory for better parallelism on the job's 4 DPUs
yellow_df = yellow_df.repartition(4 * 4).cache()

## Apply transformations ##

if len(yellow_df.columns) == 0:
    # Yellow DataFrame has no cols. Abort.
    job.commit()
    sys.exit("No new data to process.")

# Rename look-up columns and change data types as needed. Convert into Spark DataFrames.

pu_taxi_zone_df = taxi_zone_dyf.apply_mapping([
    ("locationid", "bigint", "pu_locationid", "bigint"), 
    ("borough", "string", "pu_borough", "string"), 
    ("zone", "string", "pu_zone", "string"),
    ("service_zone", "string", "pu_service_zone", "string")]).toDF()

do_taxi_zone_df = taxi_zone_dyf.apply_mapping([
    ("locationid", "bigint", "do_locationid", "bigint"), 
    ("borough", "string", "do_borough", "string"), 
    ("zone", "string", "do_zone", "string"),
    ("service_zone", "string", "do_service_zone", "string")]).toDF()

payment_type_df = payment_type_dyf.apply_mapping([
    ("id", "bigint", "payment_type_id", "bigint"), 
    ("name", "string", "payment_type_name", "string")]).toDF()
    
rate_code_df = payment_type_dyf.apply_mapping([
    ("id", "bigint", "ratecode_id", "bigint"), 
    ("name", "string", "ratecode_name", "string")]).toDF()


# Join Yellow table with look-ups, add new cols, sort by year and month, then drop unnecessary cols

yellow_opt_df = (yellow_df
             .join(broadcast(pu_taxi_zone_df), yellow_df["pulocationid"] == pu_taxi_zone_df["pu_locationid"])
             .join(broadcast(do_taxi_zone_df), yellow_df["dolocationid"] == do_taxi_zone_df["do_locationid"])
             .join(broadcast(payment_type_df), yellow_df["payment_type"] == payment_type_df["payment_type_id"])
             .join(broadcast(rate_code_df), yellow_df["ratecodeid"] == rate_code_df["ratecode_id"])
             .withColumn("pu_datetime", to_timestamp(col("tpep_pickup_datetime"), "yyyy-MM-dd HH:mm:ss"))
             .withColumn("do_datetime", to_timestamp(col("tpep_dropoff_datetime"), "yyyy-MM-dd HH:mm:ss"))
             .withColumn("pu_year", year("pu_datetime"))
             .withColumn("pu_month", month("pu_datetime"))
             .withColumn("pu_day", dayofmonth("pu_datetime"))
             .orderBy("pu_year", "pu_month", "pu_day")
             .drop("store_and_fwd_flag",
                   "pulocationid",
                   "dolocationid",
                   "paymenttype.payment_type",
                   "ratecodeid",
                   "tpep_pickup_datetime",
                   "tpep_dropoff_datetime"
                  ))

# Partition the data and convert to Parquet
# Set Parquet's Row Group size: 24, 32, and 64MB are reasonable values.
blockSize = 1024 * 1024 * 32      #32MB

(yellow_opt_df
 .write
 .mode("append") # We'll use "append" mode instead of "overwrite" as we'll use job bookmarks.
 .format("parquet")
 .option("parquet.block.size", blockSize)
 .partitionBy("pu_year", "pu_month")
 .save("s3://{}/data/prod/nyctaxi/yellow_rpt/".format(your_bucket_name)))

### Job commit

job.commit()