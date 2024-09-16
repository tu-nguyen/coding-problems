-- Title: Easy SQL: Rounding Decimals
-- Rank: 8 kyu
-- Language Version: PostgreSQL 9.6

-- Instructions --
-- Given the following table 'decimals':
-- ** decimals table schema **
-- id
-- number1
-- number2
-- Return a table with two columns (number1, number2) where the values in number1 have been rounded down and the values in number2 have been rounded up.
--
-- Solution --
select 
  floor(number1) as number1, 
  ceil(number2) as number2
from decimals

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
    
    it "should return a number1 column" do
      expect(results.first.keys).to include(:number1)
    end
    
    it "should return a number2 column" do
      expect(results.first.keys).to include(:number2)
    end
 end
end