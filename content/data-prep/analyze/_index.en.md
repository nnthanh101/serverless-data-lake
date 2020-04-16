---
title: Transformed Data & Athena
weight: 230
pre: "<b>2.3. </b>"
---

# 3.3. Explore Optimized Dataset

![Data Lake Architecture](/images/modules/analyze.png?width=50pc)

> {{%expand "Improvement in Query Performance and reduction of Data Scanned" %}}
In the previous step, you created a new Dataset that is optimized for Querying and Reporting. Now, it's time to test the optimizations you've done using SQL queries in Amazon Athena. What tangible **improvement in query performance** and **reduction of data scanned** have your optimizations achieved?

Let's find out by performing the following steps.
{{% /expand%}}

### 3.3.1 Catalog Optimized Data with an AWS Glue Crawler

🎯To be able to query the new optimized NYC Taxi trips dataset with Amazon Athena, we need to catalog the dataset using an AWS Glue Crawler.

1. Navigate to the [AWS Glue console](https://ap-southeast-1.console.aws.amazon.com/glue/home?region=ap-southeast-1#catalog:tab=crawlers)
2. In the left menu, click **Crawlers** → **Add crawler**
3. On **Crawler info** step, enter crawler name **nyctaxi-optimized-crawler** and write a description. Click **Next**.
4. On **Data store** step...
   
    a. Choose a data store: `S3` then choose `Specified path in my account`

    b. In Include path, copy-and-paste an NYC Taxi dataset S3 URL:

	```
    s3://serverless-data-lake-XXX/data/staging/nyctaxi/yellow_opt/
    ```

    Note: replace `serverless-data-lake-XXX` with your actual bucket's name.
	
    c. Click **Next**
    
    d. **Add another data store**, select **Yes**. Click **Next**, again.
	
    e. Repeat steps **(a.)** to **(c.)** for the following NYC Taxi Dataset S3 path:

	```
    s3://serverless-data-lake-XXX/data/prod/nyctaxi/yellow_rpt/
    ```

    Note: replace `serverless-data-lake-XXX` with your actual bucket's name.

    f. **Add another data store**, select **No**. Click **Next**, again.

5. On **IAM role** step...

	a. Click `Choose an existing IAM role`

	b. In **IAM Role** menu, choose `AWSGlueCrawlerRole-nyctaxi`
6. On **Schedule** step, click **Next**
7. On **Output** step...
	
    a. For **Database**, select `nyctaxi`.
	
    b. Expand **Configuration options (optional)** → select `Add new columns only`
	
    We choose this option when we plan on making changes to the table schema manually later on. In such a case, we do not want the AWS Glue Crawler to override our changes in subsequent runs.
	
	c. Click **Next**

8. On **Review all steps**, click **Finish**
9. Finally, click on the green **Run it now?** prompt at the top of the crawlers page.


> ✍️ The Crawler will run over the new optimized NYC Taxi trips dataset. It will then create a new table, called **yellow_opt** in the AWS Glue data catalog.

> {{%expand "Note that the path data/prod/nyctaxi/yellow_rpt/ does NOT exist yet!" %}}
Why do you need to add this S3 path?
Later on, in the exercise 'Advanced Exercise: AWS Glue Job Bookmarks', we'll generate a new optimized dataset for **production use** under that path. Then, we'll need to crawl it and catalog it. In a real scenario, you may choose to create a separate Crawler to crawl that Production Dataset path specifically. However, to save time and avoid repetition in this lab, we'll use a single Crawler – the one you're creating here – to crawl both Datasets.
{{% /expand%}}

> 🚀Let's take a look at what the Crawler created.

1. In the left menu, under **Data Catalog**, click **Tables**

2. Click on the **yellow_opt** table to show the **Table properties** and **Schema**

3. Scroll down, examine Table **Schema**. Notice the many new fields added. Also notice two new fields **pu_year** and **pu_month** and how they were identified as partitioning columns.