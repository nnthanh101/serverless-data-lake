---
title: Installation and Configuration
weight: 30
pre: "<b>1.3. </b>"
---


> 1. **Prerequisites**

* [x] [Create an **Twitter App**](https://developer.twitter.com/en/apps)
  * [ ] 
* [x] [Creating a **EC2 Key Pair**](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair)
  * [ ] ~~TWITTER_ACCESS_TOKEN~~
  * [ ] ~~TWITTER_ACCESS_TOKEN_SECRET~~
  * [ ] ~~TWITTER_CONSUMER_KEY~~
  * [ ] ~~TWITTER_CONSUMER_SECRET~~


> 2. Launch the **Serverless Data Lake Stack**

* [x] [Launch the CloudFormation Stack](https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/quickcreate?templateUrl=https%3A%2F%2Fserverless-data-lake.s3-ap-southeast-1.amazonaws.com%2Fai-driven-social-media-dashboard.template&stackName=Social-Listening&param_ApplicationName=AI-Driven-Social-Media&param_AuthAccessToken=TWITTER_ACCESS_TOKEN&param_AuthConsumerKey=TWITTER_CONSUMER_KEY&param_InstanceKeyName=EC2-Key-Pair&param_LatestAmiId=%2Faws%2Fservice%2Fami-amazon-linux-latest%2Famzn2-ami-hvm-x86_64-gp2&param_PublicSubnet1CIDR=10.10.0.0%2F24&param_TwitterLanguages='en'%2C'fr'%2C'vi'&param_TwitterTermList='AWS'%2C'VPC'%2C'EC2'%2C'RDS'%2C'S3'%2C'COVID-19'&param_VpcCIDR=10.10.0.0%2F18)

* {{%expand "CloudFormation >> Stacks >> Parameters" %}}
| **Parameter**                     | **Default**          | **Description**    |
|-----------------------------------|----------------------|----------------------|
| **Tweets Configuration**          |                      |                      |
| *TwitterTermList*                 | \'AWS\',\'VPC\',\'EC2\',\'RDS\',\'S3\',\'COVID-19\'  | A comma-delimited *list of terms* for which the solution will monitor tweets. For example: 'AWS', 'COVID-19'.  |
| *TwitterLanguages*                | \'en\',\'fr\',\'vi\' | A *list of language codes* for incoming tweets. Note that the format is single quotation marks and comma separated (for multiple values).  |
| **AWS Environment Parameters**    |                      |                      |
| *ApplicationName*                 | AI-Driven-Social-Media    | The *name of the application*. This name is used to name or tag resources that the solution creates.  |
| *VPC CIDR Block*                  | 10.10.0.0/18      | CIDR block for the solution created VPC. You can modify the VPC and subnet CIDR address ranges to avoid collisions with your network.  |
| *PublicSubnet1CIDR*               | 10.10.0.0/24     | CIDR block for the solution's VPC subnet created in AZ1.  |
| **Twitter API Parameters**        |                      |                      |
| *AuthAccessToken*                 | ~~TWITTER_ACCESS_TOKEN~~  | The *access token* used to call Twitter.  |
| *AuthAccessTokenSecret*           | ~~TWITTER_ACCESS_TOKEN_SECRET~~ | The *access token secret* used to call Twitter.  |
| *AuthConsumerKey*                 | ~~TWITTER_CONSUMER_KEY~~  | The *consumer key* used to access Twitter.  |
| *AuthConsumerSecret*              | ~~TWITTER_CONSUMER_SECRET~~  | The consumer key secret used to access Twitter.  |
| **Other parameters**              |                      |                      |
| *InstanceKeyName*                 | EC2-Key-Pair         | Public/private key pair, which allows you to connect securely to the solution's instance after it launches. When you created an AWS account, this is the key pair you created in your preferred region.  |
| *LatestAmiId*                     | /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2               |The ID of the latest Amazon Machine Image used for the solution's Amazon EC2 instance. **Important**: Do not change this parameter's default value.  |
{{% /expand%}}

> 3. Auto-generated Resources & Outputs from CloudFormation stack

* [x] VPC
* [x] TwitterStreamingReader Server
* [x] Kinesis Firehose
  * [x] IngestionFirehoseStream
  * [x] EntitiesFirehoseStream
  * [x] SentimentFirehoseStream
* [x] AWS Glue: `ai_driven_social_media_dashboard`
  * [ ] 	tweets
* [ ] Lambda
  * [ ] LambdaS3EventCreationCustomResource
  * [ ] SocialMediaAnalyticsLambda
* [ ] IAM & SecretsManager
  * [ ] 