-- Title: Easy SQL: Square Root and Log
-- Rank: 8 kyu
-- Language Version: SQL PostgreSQL 9.6

-- Instructions --
-- Given the following table 'decimals':

-- ** decimals table schema **

-- id
-- number1
-- number2
-- Return a table with two columns (root, log) where the values in root are the square root of those provided in number1 and the values in log are changed to a base 10 logarithm from those in number2.
--
-- Solution --
select sqrt(number1) as root, log(number2) as log 
from decimals;
-- Test Case --
results = run_sql

describe :query do
  describe "should contain keywords" do
    it "should contain SELECT" do
      expect($sql.upcase).to include("SELECT")
    end

    it "should contain FROM" do
      expect($sql.upcase).to include("FROM")
    end
  end

  describe :columns do
    it "should return 2 columns" do
      expect(results.first.keys.count).to eq 2
    end
    
    it "should return a root column" do
      expect(results.first.keys).to include(:root)
    end
    
    it "should return a log column" do
      expect(results.first.keys).to include(:log)
    end
 end
end