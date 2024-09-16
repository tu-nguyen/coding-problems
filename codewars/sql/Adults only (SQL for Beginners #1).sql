-- Title: Adults only (SQL for Beginners #1)
-- Rank: 8 kyu
-- Language Version: PostgreSQL 9.6

-- Instructions --
-- In your application, there is a section for adults only. You need to get a list of names and ages of users from the users table, who are 18 years old or older.
-- users table schema
-- name
-- age
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.
--
-- Solution --
select *
from users
where age >= 18

-- Test Case --
results = run_sql

describe :users do
   it "should return 4 users" do
    expect(results.count).to eq 4
   end
end
