-- Title: SQL Basics: Top 10 customers by total payments amount
-- Rank: 6 kyu
-- Language Version: PostgreSQL 9.6

-- Instructions --
-- For this kata we will be using the DVD Rental database.
-- Your are working for a company that wants to reward its top 10 customers with a free gift. You have been asked to generate a simple report that returns the top 10 customers by total amount spent. Total number of payments has also been requested.
-- The query should output the following columns:
-- customer_id [int4]
-- email [varchar]
-- payments_count [int]
-- total_amount [float]
-- and has the following requirements:
-- only returns the 10 top customers, ordered by total amount spent
--
-- Solution --
select a.customer_id, a.email, count(b.payment_id) as payments_count, sum(cast(b.amount as float)) as total_amount
from customer a
  inner join payment b on a.customer_id = b.customer_id
group by a.customer_id
order by 4 desc
limit 10

-- Test Case --
-- # calling run_sql will print the results and return them so that you can test data within them.
-- # if you want to test different sets of data, then its best to move this code into its own top level describe
-- # block. If you are only testing one set though, its better to set the results before you enter a describe block
-- # so that the results are presented at the top of the output.
-- results = run_sql

-- describe :query do
--   describe :columns do
--     it "should return 4 columns" do
--       expect(results.first.keys.count).to eq 4
--     end
    
--     it "should return a customer_id column" do
--       expect(results.first.keys).to include(:customer_id)
--     end
    
--     it "should return a email column" do
--       expect(results.first.keys).to include(:email)
--       expect(results.first[:email]).to include "@"
--     end
    
--     it "should return a payments_count column" do
--       expect(results.first.keys).to include(:payments_count)
--     end
    
--     describe "total_amount column" do
--       it "should have the column" do
--         expect(results.first.keys).to include(:total_amount)
--       end
    
--       it "should return a float value" do
--         expect(results.first[:total_amount]).to be_a Float
--       end
--     end
--   end
  
--   describe :rows do
--     it "should be ordered by highest total_amount" do
--       expect(results.first[:total_amount]).to eq 211.55
--     end
    
--     it "should return only 10 records" do
--       expect(results.count).to eq 10
--     end
    
--     it "should return expected results" do
--       expect(results.to_a).to eq expected
--     end
--   end
  
  
-- end