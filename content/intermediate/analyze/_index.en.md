---
title: Query Data with Athena
weight: 40
pre: "<b>4. </b>"
---

![Data Lake Architecture](/images/modules/analyze.png?width=50pc)


#### Explore transformed data using Athena

In this step we will analyze the transformed data using Athena 

Login to the Amazon Athena Console.

* GoTo: https://console.aws.amazon.com/athena/home?region=us-west-2#query
* As Athena uses the AWS Glue catalog for keeping track of data source, any S3 backed table in Glue will be visible to Athena.
* On the left panel, select '**summitdb**' from the dropdown
* Run the following query : 

```
SELECT artist_name,
         count(artist_name) AS count
FROM processed_data
GROUP BY  artist_name
ORDER BY  count desc
```

* Explore the Athena UI and try running some queries
* This query returns the list of tracks repeatedly played by devices , we will later visualize this using QuickSight

````
SELECT device_id,
         track_name,
         count(track_name) AS count
FROM processed_data
GROUP BY  device_id, track_name
ORDER BY  count desc
````