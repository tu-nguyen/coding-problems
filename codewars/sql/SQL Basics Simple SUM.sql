-- Title: SQL Basics: Simple SUM
-- Rank: 8 kyu
-- Language Version: PostgreSQL 9.6

-- Instructions --
-- For this challenge you need to create a simple SUM statement that will sum all the ages.
-- people table schema
-- id
-- name
-- age
-- select table schema
-- age_sum (sum of ages)
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.
--
-- Solution --
select sum(age) as age_sum
from people

-- Test Case --
compare_with expected do

end