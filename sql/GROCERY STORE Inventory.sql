-- Title: GROCERY STORE: Inventory
-- Rank: 7 kyu
-- Language Version: SQL PostgreSQL 9.6

-- Instructions --
-- You are the owner of the Grocery Store. All your products are in the database, that you have created after CodeWars SQL excercises!:)

-- Today you are going to CompanyA warehouse

-- You need to check what products are running out of stock, to know which you need buy in a CompanyA warehouse.

-- Use SELECT to show id, name, stock from products which are only 2 or less item in the stock and are from CompanyA.

-- Order the results by product id

-- products table schema
-- id
-- name
-- price
-- stock
-- producent
-- results table schema
-- id
-- name
-- stock
--
-- Solution --
select id, name, stock
from products
where stock <= 2 and producent = 'CompanyA'
order by id

-- Test Case --
results = run_sql

describe :query do
  describe :syntax do
    it "should contain SELECT" do
      expect($sql.upcase).to include("SELECT")
    end
    
    it "should contain WHERE" do
      expect($sql.upcase).to include("WHERE")
    end
    
    it "should order results" do
      expect($sql.upcase).to include("ORDER BY")
    end
  end

  describe :columns do
    it "should return 3 columns" do
      expect(results.first.keys.count).to eq 3
    end
    
    it "should contain id column" do
      expect(results.first.keys).to include(:id)
    end
    
    it "should contain name column" do
      expect(results.first.keys).to include(:name)
    end
    
    it "should contain stock column" do
      expect(results.first.keys).to include(:stock)
    end
  end
  
end