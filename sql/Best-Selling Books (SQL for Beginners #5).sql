-- Title: Best-Selling Books (SQL for Beginner #5)
-- Rank: 7 kyu
-- Language Version: SQL PostgreSQL 9.6

-- Instructions --
-- You work at a book store. It's the end of the month, and you need to find out the 5 bestselling books at your store. Use a select statement to list names, authors, and number of copies sold of the 5 books which were sold most.

-- books table schema

-- name
-- author
-- copies_sold
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

-- This kata is part of a collection of SQL challenges for beginners. 
--
-- Solution --
select *
from books
order by copies_sold desc
limit 5

-- Test Case --
--# Run SQL
results = run_sql

--# Tests
describe :books do
   it "should return 5 books" do
    expect(results.count).to eq 5
   end
end