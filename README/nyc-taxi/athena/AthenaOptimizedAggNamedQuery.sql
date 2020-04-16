/* nyctaxi:opt:sample_agg_qry */ 
/* Sample aggregation query re-written to work on optimized dataset.
   The query takes ~3.5 secs to run and scans only ~62MB of data.
   We've achieved 12x speedup and 25% 'data scanned' cost reduction 
   compared to raw dataset query.
*/
 SELECT pu_year,
        pu_month,
        pu_day,
        hour(pu_datetime) AS pu_hour,
        round(avg(tip_amount), 2) AS avg_tip_amount,
        round(avg(trip_distance), 2) AS avg_trip_distance,
        count(tip_amount) AS trip_count
   FROM yellow_opt
   WHERE cast(pu_year AS BigInt) = 2017 
   AND cast(pu_month AS BigInt) = 1 
   GROUP BY pu_year, pu_month, pu_day, hour(pu_datetime)
   ORDER BY pu_year, pu_month, pu_day, hour(pu_datetime)