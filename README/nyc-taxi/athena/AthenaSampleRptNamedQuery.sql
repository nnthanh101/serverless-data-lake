/* nyctaxi:raw:sample_report_qry */ 
/* A typical reporting query on Raw Data. 
   On the Raw Dataset, this query takes ~48 secs to complete. 
   Also, Athena needs to scan the entire ~165MB of compressed Raw Data.
*/ 
WITH yellow AS 
     (SELECT Date_parse(yellow.tpep_pickup_datetime, '%Y-%m-%d %H:%i:%s') AS
             pu_datetime,
             yellow.*
     FROM   yellow)
SELECT pu_datetime,
       total_amount,
       tip_amount,
       paymenttype.name,
       ratecode.name
FROM   yellow
       join paymenttype ON yellow.payment_type = paymenttype.id
       join ratecode ON yellow.ratecodeid = ratecode.id
       join taxizone AS pu_taxizone ON yellow.pulocationid = pu_taxizone.locationid
       join taxizone AS do_taxizone ON yellow.dolocationid = do_taxizone.locationid
WHERE  Year(pu_datetime) = 2017
       AND Month(pu_datetime) = 1
       AND Day(pu_datetime) BETWEEN 1 AND 10
ORDER  BY Year(pu_datetime),
          Month(pu_datetime),
          Day(pu_datetime)