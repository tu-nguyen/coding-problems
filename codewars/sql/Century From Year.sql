-- Title: Century From Year
-- Rank: 8 kyu
-- Language Version: PostgreSQL 9.6

-- Instructions --
-- Introduction
-- The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.
-- Task :
-- Given a year, return the century it is in.
-- Input , Output Examples ::
-- centuryFromYear(1705)  returns (18)
-- centuryFromYear(1900)  returns (19)
-- centuryFromYear(1601)  returns (17)
-- centuryFromYear(2000)  returns (20)
-- In SQL, you will be given a table years with a column yr for the year. Return a table with a column century.
-- Hope you enjoy it .. Awaiting for Best Practice Codes
-- Enjoy Learning !!!
--
-- Solution --
select ceil(yr / 100.00) as century
from years

-- Test Case --
items = DB[:years]

basic_tests = [
  [1705, 18],
  [1900, 19],
  [1601, 17],
  [2000, 20],
  [356, 4],
  [89, 1]
]

basic_tests.each do |x|
  items.insert(:yr => x[0])
end

results = run_sql.to_a

describe :basic_tests do
  basic_tests.each_with_index do |x, i|
    it "Test for year #{x[0]}" do
      expect(results[i][:century]).to eq x[1]
    end
  end
end