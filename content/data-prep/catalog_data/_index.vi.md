---
title: Catalog Data with Crawler
weight: 210
pre: "<b>2.1. </b>"
---

# 2.1. Explore Raw Dataset

![Data Lake Architecture](/images/modules/catalog.png?width=50pc)

> {{%expand "AWS Glue Crawlers explore a Dataset is understanding its Schema and its other properties." %}}
A Crawler scans your data, classifying its format (.csv, .tsv, ...) and inferring its schema including fields and potential datatypes. Crawlers also collect useful metadata such as total record count, total dataset size, number of files scanned, type of compression used, and more. After a crawler completes, it writes a dataset's schema and properties to the AWS Glue Data Catalog.
{{% /expand%}}

> {{%expand "Glue IAM Role" %}}
{{% /expand%}}


### 2.2.1. Create and run an AWS Glue Crawler

🎯Let's run an AWS Glue crawler on the raw NYC Taxi trips dataset.

 1. Navigate to the **AWS Glue** console
 2. In the left menu, click **Crawlers** → **Add crawler**
 3. On **Crawler info** step, enter crawler name **_nyctaxi-raw-crawler_** and write a description.
 4. Click **Next**
   
 5. On **Data stores** step...
   
    a. Choose a data store: `S3` 

    b. Choose `Specified path in my account`

	c. In Include path, copy-and-paste an NYC Taxi dataset S3 URL:
	```
    s3://serverless-data-lake-XXX/data/raw/nyctaxi/
    ```

    Note: replace ~~`serverless-data-lake-XXX`~~ with your actual bucket's name.

	d. Click Next then Next once again.

1. On **IAM Role** step...
   
    a. Click `Choose an existing IAM role`

    b. In IAM role menu, choose `AWSGlueCrawlerRole-nyctaxi`

    c. Click **Next**

2. On **Schedule** step, click **Next**

3. On **Output** step...

    a. Click **Add database** → enter `nyctaxi` as the name → click **Create**

    b. Expand Configuration options (optional) → select `Add new columns only`

    c. Click Next

4. On **Review all steps**, click **Finish**.

5.  Finally, click on the green **Run it now?** prompt at the top of the Crawlers page.


> ✍️ Your crawler should immediately start. Upon completion, it adds four tables in the **nyctaxi** database in your AWS Glue data catalog: **yellow** , **paymenttype** , **ratecode** , and **taxizone**.

### 2.2.2. Explore Table Schema and Metadata

🎯Now that we have cataloged the raw NYC Taxi trips dataset using a Crawler, let's explore the Crawler's output in the AWS Glue Data Catalog.

1. Navigate to the [AWS Glue console](https://console.aws.amazon.com/glue/home?region=ap-southeast-1#catalog). 
2. In the left menu, under **Data Catalog** , click **Tables** --> show a list of NYC Taxi dataset tables cataloged by your crawler: `yellow`, `paymenttype`, `ratecode`, and **taxizone**.
3. Click on the **yellow** table to show the Table properties and Schema

    a. **Classification**, showing the table was classified as `csv`

	b. **objectCount**, showing how many files were found

	c. **sizeKey**, showing total dataset size

	d. **recordCount**, showing total number of records

	e. **compressionType**, showing the files are compressed in `bzip2`

4. Scroll down, examine Table **Schema**. Fields have been identified along with their potential Datatypes. You can manually change any Datatype.


### 2.2.3. Query Raw Data with Amazon Athena

> {{%expand "Proposing Amazon Athena along with Amazon QuickSight." %}}

🎯We know that Unicorn-Taxi's business End-Users need a solution for Ad-hoc Analysis, Reporting, and Visualization. Evaluating the options based on requirements, We decide on proposing Amazon Athena along with Amazon QuickSight.

**Amazon Athena** is a Serverless Interactive Query Service that makes it easy to analyze data in Amazon S3 using standard SQL. It integrates with the AWS Glue Data Catalog and takes advantage of the Metadata registered by AWS Glue crawlers. 
**Amazon QuickSight** is a fast, Cloud-powered BI Service that makes it easy to build Visualizations, perform Ad-hoc Analysis,
and quickly get business insights from our data.

Because Amazon Athena will act as our Data Lake's Querying Service, We decide to use Athena to explore the raw NYC Taxi Trips Dataset. The goal here is to see how Amazon Athena performs on the Raw Dataset and establish a performance baseline.
{{% /expand%}}

Let's run two SQL queries in Amazon Athena: a sample reporting query ( **_sample_report_qry_** ) and a sample aggregation query ( **_sample_agg_qry_** ). Both queries represent typical reporting
and analytics queries that Unicorn-Taxi's business end users may want to run on the dataset.

1. Navigate to **Amazon Athena** console, click **Get Started**. Click **X** to skip tutorial.
2. Ensure database `nyctaxi` is selected, and the 4 tables are listed: `yellow`, `paymenttype`, `ratecode`, and `taxizone`.
3. Click on the tab **Saved Queries**
4. In the search field, type `nyctaxi:raw`
5. Click on the `AthenaSampleRptNamedQuery-` query to open in Athena Query Editor.
Note: After opening the query, [review the comment before the SQL statement](https://github.com/nnthanh101/serverless-data-lake/blob/nyc-taxi/README/nyc-taxi/athena/AthenaSampleRptNamedQuery.sql).
1. Click **Run query**

2. Note: Query **Run time** and **Data scanned**. Copy and paste it into an open text file for later comparison.
`(Run time: 48.74 seconds, Data scanned: 164.98 MB)`

1. Repeat **steps 3- 7** for query **[AthenaSampleAggQuery-](https://github.com/nnthanh101/serverless-data-lake/blob/nyc-taxi/README/nyc-taxi/athena/AthenaSampleAggQuery.sql)**

✍️ The *Query Run time* and *Data scanned* values you obtained are a result of running the queries directly on the **Raw Dataset**. Later on, we'll create an **Optimized Dataset** and query it again. And then, we'll be able to compare Query Run times and Data scanned on Raw Dataset versus Optimized Dataset.
