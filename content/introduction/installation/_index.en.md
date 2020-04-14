---
title: Setup Prerequisite Resources
weight: 20
pre: "<b>1.2. </b>"
---


### 1.2.1. Get your **AWS account** ready!

You have received AWS credentials; make sure you have sufficient privileges in your AWS account.

### 1.2.2. Setup Pre-requisite Resources

We will use an AWS CloudFormation template to setup a number of required AWS Resources.

1. [Sign into your AWS account with your credentials](console.aws.amazon.com)
2. Navigate to the **AWS CloudFormation** console >> Copy and paste the following URL:
```
https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/quickcreate?templateUrl=https%3A%2F%2Fjob4u.s3-ap-southeast-1.amazonaws.com%2Fserverless-data-lake%2Fserverless-dataprep-glue.yaml&stackName=serverless-data-lake
```
3. Check next to **I acknowledge that AWS CloudFormation might create IAM resources with custom names**
4. Click **Create.** The AWS CloudFormation stack takes **about 7 minutes** to create.
5. After the stack creates successfully, go to the **Outputs** tab
6. Look for the key **S3BucketName**. **Copy and keep** its value. This is your Amazon S3 bucket's name that we will use throughout the workshop.

### 1.2.3. Created Resources from CloudFormation

| Key | Value | Description |
|-----|-------|-------------|
| S3BucketName | serverless-data-lake-XXX | New Data Lake S3 Bucket|
| IAM Roles & Policies |  | For AWS Glue, Amazon Athena, Amazon SageMaker, and AWS Lambda |
| GlueDevEndpoint | nyctaxi-dev-endpoint-serverless-data-lake | **AWS Glue** development endpoint |
| Athena*Query |  | A number of **named Queries in Amazon Athena** |
| CopyDataFunction |  | An **AWS Lambda Function** that can copy NYC Taxi Trips - Raw Dataset files into your Amazon S3 Bucket |


Finally, the **NYC Taxi Trips Raw Dataset is copied** into your Amazon S3 bucket.
