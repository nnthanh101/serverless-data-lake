---
title: Transform Data & Glue
weight: 20
pre: "<b>2.2. </b>"
---

# 2.2. Create an Optimized Dataset

![Data Lake Architecture](/images/modules/transform.png?width=50pc)


> {{%expand "Transform Data using Apache Spark & AWS Glue Development Endpoints" %}}
After running test SQL queries in Amazon Athena, you verify that you can make the following improvements to the NYC Taxi trips dataset. Ultimately, these improvements together reduce per-query Amazon Athena cost and improve Unicorn-Taxi's Business Users' eXperience.

- **Convert the Dataset from CSV** to a compressed and splittable columnar file format, such as **Parquet**. This enables Amazon Athena to optimize query execution by avoiding scanning columns that are not needed by your query and rows that are filtered out by your query.
- **Partition the Dataset** in Amazon S3 by year and month into Hive-style partitions. The Partitioning Scheme enables queries that filter on a specific Year or Month to avoid scanning unnecessary data for other Years and Months, thereby acting as a crude index.
- **De-normalize the Dataset** by joining the primary fact table **_yellow_** with the dimension tables **_taxizone_** , **_ratecode_** , and **_paymenttype_**. This creates a new table that is simpler to query and run reports on.
- **Create new columns and drop unnecessary columns**.

To develop and test code to apply such transformations on the large NYC Taxi trips dataset, you consider using an **Apache Spark** environment that can access and manipulate your data directly in Amazon S3. You decide to take advantage of **AWS Glue Development Endpoints** for that purpose. Also, instead of setting up and managing your own Zeppelin or Jupyter Notebook Server, you leverage AWS Glue's ability to launch a fully-managed Jupyter Notebook Instance for interactive ETL and Machine Learning development. Your Jupyter Notebook will use your AWS Glue Development Endpoint to run your ETL code written in **PySpark** or **Scala**.

Let's go through the steps to setup your interactive ETL Notebook Environment and apply the Data Transformations.
{{% /expand%}}

> {{%expand "Ensure your AWS Glue Dev endpoint is READY" %}}
The AWS Glue Dev Endpoint was automatically created for you by the AWS CloudFormation template your ran in section "1.2.1. Get your AWS account ready".

1. Navigate to the [AWS Glue console](https://ap-southeast-1.console.aws.amazon.com/glue/home?region=ap-southeast-1)
2. In the left menu, under **ETL**, click **Dev endpoints**
3. Verify there is a dev endpoint named **nyctaxi-dev-endpoint-**
4. Verify that the status is **READY**
{{% /expand%}}


### 2.3.1. Create an Amazon SageMaker Notebook instance

Proceed to create a SageMaker Notebook instance. Follow these steps.

1. In the left menu, under [**ETL** → **Dev endpoints** , click **Notebooks**](https://ap-southeast-1.console.aws.amazon.com/glue/home?region=ap-southeast-1#etl:tab=notebooks)
2. Click **Create notebook**
3. For **Notebook name**, enter `nyctaxi-notebook`
4. For **Attach to development endpoint**, select `nyctaxi-dev-endpoint-`
5. Select **Choose an existing IAM role** then choose
    `AWSGlueServiceSageMakerNotebookRole-nyctaxi_`
6. Click **Create notebook**. This will take you back to the **Notebooks** page.
7. Click the **Refresh** button, if needed. You should notice a notebook with the name **`aws-glue-nyctaxi-notebook`** and the status **Starting**.

> ✍️ The Amazon SageMaker notebook should take **about 6 minutes** to transfer into a **Ready** status.


### 2.3.2. Interactively author and run ETL code in Jupyter

> 🎯 First, We'll download the ETL Notebook we prepared for you; then upload the Notebook to your own Amazon SageMaker Notebook, from the AWS Glue console.

1. Download Notebook file **[nyctaxi_raw_dataset_etl.ipynb](https://github.com/nnthanh101/serverless-data-lake/blob/nyc-taxi/README/nyc-taxi/nyctaxi_raw_dataset_etl.ipynb)**
2. Navigate to the [**AWS Glue** console](https://ap-southeast-1.console.aws.amazon.com/glue/home?region=ap-southeast-1#etl:tab=notebooks).  In the left menu, under **ETL** → **Dev endpoints**, click **Notebooks**
4. Select **aws-glue-nyctaxi-notebook**, then click **Open notebook** and then **OK**. A new browser tab will open showing **Jupyter** interface
5. In **Jupyter**, in the upper right corner, click the **Upload** button
6. Browse to and select **nyctaxi_raw_dataset_etl.ipynb** , then in Jupyter, click **Upload** again. After upload, the Notebook should appear in Jupyter.
7. Click on **nyctaxi_raw_dataset_etl.ipynb** to open Notebook. Spend a few moments to have an overview of the documented ETL Code and what it does.

> 🎯Next, We'll edit the **ETL code** in the Notebook and then run it on the Raw NYC Taxi Trips Dataset.

1. In **Jupyter**, ensure the `nyctaxi_raw_dataset_etl.ipynb` notebook is open
2. In the **first PySpark code cell**, look for the variable ~~**your-datalake-bucket**~~. Set the value of that string variable to **your own Amazon S3 bucket’s name** `serverless-data-lake-XXX`
3. Click the **Save and Checkpoint** button to save the change you made to your notebook.
4. Click on the **Cells** menu → **Run All**
5. This will run *ETL code* in the Notebook. The code finally creates a new dataset under the Amazon S3 prefix in your own account:
    ```
    s3://serverless-data-lake-XXX/data/staging/nyctaxi/yellow_opt/
    ```
    Note: replace `serverless-data-lake-XXX` with your actual bucket's name.

> ✍️The Notebook should take about 8 minutes to complete.

