---
title: Architecture & Dataset
weight: 10
disableToc: true
pre: "<b>1.1. </b>"
---


![Data Lake Architecture](/images/architecture/architecture.png?width=50pc)


> [**NYC Taxi Trips** Dataset](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page): for practical purposes, we'll work with a **Simplified Raw** Dataset.

| Original Raw Dataset | Simplified Raw Dataset |
|-----------------------------|--|
| Green and Yellow Taxi + FHV | Only **Yellow** Taxi + few look-ups |
| Years 2009 to 2019 | Jan to March 2017 |
| ~1.6Bn rows        | ~2M rows |
| 215 files          | 3 files |
| 253 GB total       | 2.5 GB+ uncompressed |
|             | **Ready in a publicly accessible Amazon S3 bucket** |