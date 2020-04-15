/* nyctaxi:raw:sample_agg_qry */ 
/* This is a query that calculates avg trip amount, avg trip distance, 
   and count of trips grouped by year, month, day, and hour.
   This query takes about 38 seconds to execute.
   Also, Athena needs to scan the entire ~165MB of compressed Raw Data.
*/
WITH yellow2 AS 
     (SELECT Date_parse(yellow.tpep_pickup_datetime, '%Y-%m-%d %H:%i:%s') AS
             pu_datetime,
             yellow.tip_amount,
             yellow.trip_distance,
             yellow.payment_type
     FROM   yellow)
SELECT Year(yellow2.pu_datetime)            AS pu_year,
       Month(yellow2.pu_datetime)           AS pu_month,
       Day(yellow2.pu_datetime)             AS pu_day,
       Hour(yellow2.pu_datetime)            AS pu_hour,
       Round(Avg(yellow2.tip_amount), 2)    AS avg_tip_amount,
       Round(Avg(yellow2.trip_distance), 2) AS avg_trip_distance,
       Count(yellow2.tip_amount)            AS trip_count
FROM   yellow2
WHERE  Year(yellow2.pu_datetime) = 2017
       AND Month(yellow2.pu_datetime) = 1
GROUP  BY Year(yellow2.pu_datetime),
          Month(yellow2.pu_datetime),
          Day(yellow2.pu_datetime),
          Hour(yellow2.pu_datetime)
ORDER  BY Year(yellow2.pu_datetime),
          Month(yellow2.pu_datetime),
          Day(yellow2.pu_datetime),
          Hour(yellow2.pu_datetime) 