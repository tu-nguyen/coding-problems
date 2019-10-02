-- Title: SQL Grasshopper: Select Columns
-- Rank: 8 kyu
-- Language Version: PostgreSQL 9.6

-- Instructions --
-- #Greetings Grasshopper!# Using only SQL, write a query that returns all rows in the custid, custname, and custstate columns from the customers table.
--
-- Solution --
select custid, custname, custstate
from customers

-- Test Case --
results
= run_sql

describe :results do
  it "should return 20 items" do
    expect
(results.count).to eq 20
end
  
  it "should contain only 3 columns" do
    expect
(results.first.keys.count).to eq 3
end
  
  it "should not contain custard column" do
    expect
(results.first.keys).not_to include
(:custard)
end
end