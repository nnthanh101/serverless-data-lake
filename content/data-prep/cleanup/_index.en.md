---
title: Cleanup
weight: 70
pre: "<b>7. </b>"
---

Failing to do this will result in incuring AWS usage charges.

Make sure you bring down / delete all resources created as part of this lab

#### Resources to delete
* Kinesis Firehose Delivery Stream
	* GoTo: https://console.aws.amazon.com/firehose/home?region=ap-southeast-1#/
	* Delete Firehose:  **social-listening-stream**
* Lambda
	* GoTo: https://console.aws.amazon.com/lambda/home?region=ap-southeast-1
	* Navigate to list of functions and select **top5Songs**.
	* Under **Actions** drop down menu, select **Delete**.
* Glue Database
	* GoTo: https://console.aws.amazon.com/glue/home?region=ap-southeast-1#catalog:tab=databases
	* Delete Database: **summitdb**
* Glue Crawler
	* GoTo: https://console.aws.amazon.com/glue/home?region=ap-southeast-1#catalog:tab=crawlers
	* Delete Crawler: **summitcrawler**
* Glue Dev Endpoint
	* GoTo: https://console.aws.amazon.com/glue/home?region=ap-southeast-1#etl:tab=devEndpoints
	* Delete endpoint: **devendpoint1**
* Sagemaker Notebook
	* You may wish you download the notebook file locally on your laptop before deleting the notebook)
	* GoTo: https://console.aws.amazon.com/glue/home?region=ap-southeast-1#etl:tab=notebooks
	* Delete Notebook: **aws-glue-notebook1**
* Delete IAM Role
	* GoTo: https://console.aws.amazon.com/iam/home?region=ap-southeast-1#/roles
	* Search for AWSGlueServiceRoleDefault
	* Delete Role: **AWSGlueServiceRoleDefault**
	* Search for top5Songs in search box 
	* Select and delete this role. [top5Songs-role-<id>]
* Delete S3 bucket
	* GoTo: https://s3.console.aws.amazon.com/s3/home?region=ap-southeast-1
	* Delete Bucket: **your-datalake-bucket**
* Delete Cognito Setup :
	* Goto: https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/
	* Click: **Kinesis-Data-Generator-Cognito-User**
	* Click: **Actions** > **DeleteStack**
	* On confirmation screen: Click: **Delete**
* Close QuickSight account
	* GoTo: https://us-east-1.quicksight.aws.amazon.com/sn/admin#permissions
	* Click: **Unsubscribe**
* Cognito Userpool
	* GoTo: https://ap-southeast-1.console.aws.amazon.com/cognito/users/?region=ap-southeast-1#/