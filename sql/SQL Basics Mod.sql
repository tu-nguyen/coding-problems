-- Title: SQL Basics: Mod
-- Rank: 8 kyu
-- Language Version: PostgreSQL 9.6

-- Instructions --
-- Given the following table 'decimals':
-- ** decimals table schema **
-- id
-- number1
-- number2
-- Return a table with one column (mod) which is the output of number1 modulus number2.
--
-- Solution --
select number1 % number2 as mod
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
    it "should return 1 column" do
      expect(results.first.keys.count).to eq 1
    end
    
    it "should return a mod column" do
      expect(results.first.keys).to include(:mod)
    end
 end
end