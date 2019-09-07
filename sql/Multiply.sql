-- Title: Multiply
-- Rank: 8 kyu
-- Language Version: SQL PostgreSQL 9.6

---- Instructions ----
-- The code does not execute properly. Try to figure out why.
-- SELECT price + amount AS total FROM items
--
---- Solution ----
SELECT price * amount AS total FROM items

---- Test Case ----
compare_with expected