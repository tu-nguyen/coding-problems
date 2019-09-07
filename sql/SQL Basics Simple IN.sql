-- Title: SQL Basics: Simple IN
-- Rank: 6 kyu
-- Language Version: SQL PostgreSQL 9.6

-- Instructions --
-- For this challenge you need to create a SELECT statement, this SELECT statement will use an IN to check whether a department has had a sale with a price over 98.00 dollars.

-- departments table schema
-- id
-- name
-- sales table schema
-- id
-- department_id (department foreign key)
-- name
-- price
-- card_name
-- card_number
-- transaction_date
-- resultant table schema
-- id
-- name
-- NOTE: sometimes a department will not not contain a sale over $98 so just resubmit.
--
-- Solution --
SELECT id, name
FROM departments
WHERE id in (SELECT department_id
            FROM sales
            WHERE price > 98)

-- Test Case --
results = run_sql

describe :query do
  describe "should contain keywords" do    
    it "should contain IN" do
      expect($sql.upcase).to include("IN")
    end
    
    it "should contain WHERE" do
      expect($sql.upcase).to include("WHERE")
    end
        
    it "should not contain EXISTS" do
      expect($sql.upcase).not_to include("EXISTS")
    end
    
    it "should not contain JOIN" do
      expect($sql.upcase).not_to include("JOIN")
    end
    
    it "should not contain DISTINCT" do
      expect($sql.upcase).not_to include("DISTINCT")
    end
    
    it "should not contain LIMIT" do
      expect($sql.upcase).not_to include("LIMIT")
    end
  end

  describe :columns do
    it "should return 2 columns" do
      expect(results.first.keys.count).to eq 2
    end
    
    it "should return an id column" do
      expect(results.first.keys).to include(:id)
    end
    
    it "should return a name column" do
      expect(results.first.keys).to include(:name)
    end
  end
end