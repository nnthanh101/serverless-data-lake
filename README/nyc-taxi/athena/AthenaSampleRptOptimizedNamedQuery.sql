/* nyctaxi:opt:sample_report_qry */ 
/* This is the reporting query re-written for the optimized dataset. 
   It takes ~16 secs to run and scans only ~20MB of data. 
   This is about 3x speed-up and 80% 'data scanned' cost reduction 
   compared to raw dataset query.
*/
SELECT pu_datetime,
       total_amount,
       tip_amount,
       payment_type_name,
       ratecode_name
FROM   yellow_opt
WHERE  Cast(pu_year AS BIGINT) = 2017
       AND Cast(pu_month AS BIGINT) = 1
       AND pu_day BETWEEN 1 AND 10
ORDER  BY pu_year,
          pu_month