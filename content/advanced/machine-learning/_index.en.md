---
title: AI & Machine Learning
weight: 310
pre: "<b>3.1. </b>"
---


> {{%expand "🎯🎯🎯 Solve a Machine Learning Problem: Perform Tip Amount Prediction for a particular Ride" %}}
So far, we have curated and optimized the NYC Taxi Dataset that can be utilized for analytics using Business Intelligence tools or by Data Science team to solve key business problems as predictions. 
**Amazon SageMaker** is a fully managed machine learning service. With Amazon SageMaker, Data Scientists and Developers can quickly and easily build and train Machine Learning Models, and then directly deploy them into a Production-ready Hosted Environment.

It is interesting to combine Glue’s Spark ML capabilities of feature engineering, orchestrating of SageMaker training, hosting model, end point creation and predictions via Glue SageMaker Notebook.

In this section, we will utilize optimized NYC Taxi dataset to perform Tip Amount prediction for a particular ride. Below are high level steps.

- **Data Cleansing** – Remove biased features (e.g. remove samples with payment_type as ‘CASH’ as most drivers don’t report tips for cash payments)
- **Feature Trend Analysis** – Understand trends in data relative to label (Tip Amount) to remove biased samples
- **Feature Engineering** – Extract features from raw data and transform features to make them suitable for training (e.g. convert day of week string to numeric and then binary vector)
- **Data Split** – Split data into Training dataset and Test dataset
- **Training and Hosting Model –** Using SageMaker Spark SDK, launch XGBoost training, model creation and endpoint creation
- **Run Predictions –** Derive predictions using Spark transform() method
{{% /expand%}}


> 🎯Interactively develop a Machine Learning model in Jupyter

1. Download [**nyctaxi_tips_prediction_xgboost.ipynb** Notebook file](https://github.com/nnthanh101/serverless-data-lake/blob/nyc-taxi/README/nyc-taxi/nyctaxi_tips_prediction_xgboost.ipynb)
2. Navigate to the [**AWS Glue console**](https://ap-southeast-1.console.aws.amazon.com/glue/home?region=ap-southeast-1#etl:tab=notebooks). In the left menu, under **ETL** → **Dev endpoints**, click **Notebooks**
3. Select `aws-glue-nyctaxi-notebook`, then click **Open notebook**. A new browser tab will open showing **Jupyter** interface
4. In **Jupyter**, in the upper right corner, click the **Upload** button 
5. Browse to and select `nyctaxi_tips_prediction_xgboost.ipynb`, then in Jupyter, click **Upload** again. After upload, the Notebook should appear in Jupyter.
6. Click on **nyctaxi_raw_dataset_etl.ipynb** to open Notebook. Ensure the kernel is set to **Sparkmagic (PySpark)** in the upper right corner.
7. **Run one cell at a time** by clicking each cell from top and clicking
8. Observe output of each Cell and also refer to documentation links provided in Notebook along with code as appropriate.


{{% notice info %}} 
You've made it! 
{{% /notice %}}