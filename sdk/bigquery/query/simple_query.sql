-- create a example temp table

WITH Players AS
 (SELECT 'gorbie' as account, 29 as level UNION ALL
  SELECT 'junelyn', 2 UNION ALL
  SELECT 'corba', 43 UNION ALL
  SELECT 'jiji', 50)

SELECT * FROM Players

-- show avg level as sub query

WITH Players AS
 (SELECT 'gorbie' as account, 29 as level UNION ALL
  SELECT 'junelyn', 2 UNION ALL
  SELECT 'corba', 43 UNION ALL
  SELECT 'jiji', 50)

SELECT account, level, (SELECT AVG(level) FROM Players) AS avg_level
FROM Players;


WITH Players AS
 (SELECT 'gorbie' as account, 29 as level UNION ALL
  SELECT 'junelyn', 2 UNION ALL
  SELECT 'corba', 43 UNION ALL
  SELECT 'jiji', 50)

SELECT account, level, (level - SELECT AVG(level) FROM Players) AS diff
FROM Players;

-- Array

SELECT [1, 2, 3] as num_arr;

SELECT ["apple", "pear", "orange"] as fruit_arr;

SELECT [true, false, true] as bool_arr;

SELECT ARRAY<FLOAT64>[1, 2, 3] as floats;

SELECT GENERATE_ARRAY(1, 50, 2) AS odds;


WITH sequences AS
  (SELECT [0, 1, 1, 2, 3, 5] AS some_numbers
   UNION ALL SELECT [2, 4, 8, 16, 32] AS some_numbers
   UNION ALL SELECT [5, 10] AS some_numbers)
SELECT some_numbers,
       some_numbers[OFFSET(0)] AS offset_1,
       ARRAY_LENGTH(some_numbers) AS len
FROM sequences;

WITH sequences AS
  (SELECT 1 AS id, [0, 1, 1, 2, 3, 5] AS some_numbers
   UNION ALL SELECT 2 AS id, [2, 4, 8, 16, 32] AS some_numbers
   UNION ALL SELECT 3 AS id, [5, 10] AS some_numbers)
SELECT id, flattened_numbers
FROM sequences, sequences.some_numbers AS flattened_numbers;


WITH sequences AS
  (SELECT [0, 1, 1, 2, 3, 5] AS some_numbers
  UNION ALL SELECT [2, 4, 8, 16, 32] AS some_numbers
  UNION ALL SELECT [5, 10] AS some_numbers)
SELECT some_numbers,
  ARRAY(SELECT x * 2
        FROM UNNEST(some_numbers) AS x) AS doubled
FROM sequences;


WITH sequences AS
  (SELECT [0, 1, 1, 2, 3, 5] AS some_numbers
   UNION ALL SELECT [2, 4, 8, 16, 32] AS some_numbers
   UNION ALL SELECT [5, 10] AS some_numbers)
   
SELECT some_numbers,
  (SELECT SUM(x)
   FROM UNNEST(s.some_numbers) x) AS sums
FROM sequences s;
