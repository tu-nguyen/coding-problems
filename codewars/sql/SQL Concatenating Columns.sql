-- Title: SQL: Concatenating Columns
-- Rank: 7 kyu
-- Language Version: SQL PostgreSQL 9.6

-- Instructions --
-- Given the table below:

-- ** names table schema **

-- id
-- prefix
-- first
-- last
-- suffix
-- Your task is to use a select statement to return a single column table containing the full title of the person (concatenate all columns together except id), as follows:

-- ** output table schema **

-- title
-- Don't forget to add spaces.
--
-- Solution --
select concat(prefix,' ',first,' ',last, ' ',suffix) as title
from names;

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
    
    it "should return a title column" do
      expect(results.first.keys).to include(:title)
    end
  end
end