---
title: Data Lake Architecture
weight: 10
disableToc: true
pre: "<b>1.1. </b>"
---


![Data Lake Architecture](/images/architecture/architecture.png?width=50pc)


> Build a Data Processing Pipeline and Data Lake

1. **Ingest and Store**: use Amazon Kinesis for real-time streaming data
2. **Catalog Data**: Use AWS Glue to automatically Catalog Datasets
3. **Transform Data**: Run interactive ETL scripts in an Amazon SageMaker Jupyter notebook connected to an AWS Glue development endpoint
4. **Analyze**: Query data using Amazon Athena
5. **Visualize**: visualize it using Amazon QuickSight
6. **Lambda**: 