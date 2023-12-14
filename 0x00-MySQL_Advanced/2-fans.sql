-- import table dump
-- Create a temporary table to store the results
-- Display the results
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
