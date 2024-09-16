-- Title: SQL Basics: Simple MIN / MAX
-- Rank: 8 kyu
-- Language Version: PostgreSQL 9.6

-- Instructions --
-- For this challenge you need to create a simple MIN / MAX statement that will return the Minimum and Maximum ages out of all the people.
-- people table schema
-- id
-- name
-- age
-- select table schema
-- age_min (minimum of ages)
-- age_max (maximum of ages)
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.
--
-- Solution --
select min(age) as age_min, max(age) as age_max
from people

-- Test Case --
results = run_sql

describe :items do
   it "should return 1 item" do
    expect(results.count).to eq 1
   end
end