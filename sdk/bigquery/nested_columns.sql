-- ARRAY NESTED TYPE

SELECT ['Xbox One', 'Xbox Series X', 'Xbox Series S'] AS consoles;

WITH consoles AS (
  SELECT ['Xbox One', 'Xbox Series X', 'Xbox Series S'] AS console_name
)
SELECT * FROM consoles;


-- STRUCT NESTED TYPE

WITH vendors AS (
  SELECT STRUCT(
    'Microsoft' AS vendor_name,
    'Xbox Series X' AS console_name
  ) AS vendor_set
)
SELECT * FROM vendors;


WITH vendors AS (
  SELECT STRUCT(
    'Microsoft' AS name,
    ['Xbox One', 'Xbox Series X', 'Xbox Series S'] AS consoles
  ) AS vendor_set
  UNION ALL
  SELECT STRUCT(
    'Nintendo' AS name,
    ['Wii U', 'Nintendo Switch', 'Nintendo Switch Lite'] AS consoles
  ) AS vendor_set
  UNION ALL
  SELECT STRUCT(
    'Sony' AS name,
    ['Playstation 3', 'Playstation 4', 'Playstation 5'] AS consoles
  ) AS vendor_set
)
SELECT * FROM vendors;

-- STRUCT NESTED TYPE > UNNESTED TYPE


WITH vendors AS (
  SELECT STRUCT(
    'Microsoft' AS name,
    ['Xbox One', 'Xbox Series X', 'Xbox Series S'] AS consoles
  ) AS vendor_set
  UNION ALL
  SELECT STRUCT(
    'Nintendo' AS name,
    ['Wii U', 'Nintendo Switch', 'Nintendo Switch Lite'] AS consoles
  ) AS vendor_set
  UNION ALL
  SELECT STRUCT(
    'Sony' AS name,
    ['Playstation 3', 'Playstation 4', 'Playstation 5'] AS consoles
  ) AS vendor_set
)
SELECT
  vendor_set.name,
  unnest_console
FROM
  vendors,
  UNNEST(vendor_set.consoles) AS unnest_console;