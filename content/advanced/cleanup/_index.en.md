---
title: Account Cleanup Instruction
weight: 320
pre: "<b>3.2. </b>"
---

Once you are done with the lab, follow the instructions below to clean-up your account.

> First, delete manually-created AWS Glue resources.

1. Navigate to the **AWS Glue** console
   
2. Go to **Databases** then select **nyctaxi**. 
   
   Click **Action**, then **Delete database**. Confirm deletion.
3. Go to **Crawlers** then select **nyctaxi-optimized-crawler**. 
   
   Click **Action** , then **Delete crawler**. Confirm deletion. 
   
   Repeat for **nyctaxi-raw-crawler**.

4. Go to **Jobs**, then select **nyctaxi-create-optimized-dataset**. 

	Click **Action**, then **Delete**. Confirm deletion.

5. Got to **Triggers**, then select **nyctaxi-process-raw-dataset**. 
   
   Click **Action**, then **Delete**. Confirm deletion.

6. Go to **Notebooks**, then select **aws-glue-nyctaxi-notebook**. 
   
   Click **Action**, then **Stop**. Wait until notebook status changes to **Stopped**. 
   
   Click **Action** again, then **Delete**.

> Finally, delete the Serverless-Data-Lake AWS CloudFormation stack to clean-up remaining resources.

7. Navigate to the [**AWS CloudFormation** console](https://ap-southeast-1.console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks?filteringText=serverless-data-lake&filteringStatus=active&viewNested=true&hideStacks=false&stackId=)
   
8. Select the `serverless-data-lake` stack

	Click **Delete**, then **Delete stack** to Confirm deletion.

9. Stack status will change to **DELETE_IN_PROGRESS**. The stack should take less than a minute to be deleted.

{{% notice note %}} 
You're DONE ✅ Cleaning-up your account! 👌
{{% /notice %}}