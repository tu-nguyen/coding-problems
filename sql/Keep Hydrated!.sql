-- Title: Keep Hydrated!
-- Rank: 8 kyu
-- Language Version: PostgreSQL 9.6

-- Instructions --
-- Nathan loves cycling.
-- Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
-- You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
-- For example:
-- time = 3 ----> litres = 1
-- time = 6.7---> litres = 3
-- time = 11.8--> litres = 5
-- You have to return 3 columns: id, hours and liters (not litres, it's a difference from the kata description)
--
-- Solution --
select id, hours, floor(hours * 0.5) as liters
from cycling

-- Test Case --
# TODO: replace with your own tests (TDD), these are just how-to examples to get you started.

# Ruby/Rspec/Sequel Example:
# While the code section is pure SQL, for testing we use Ruby & Rspec.
# Sequel (https://github.com/jeremyevans/sequel) is used to setup the database and run queries.
# The connection is already made for you, use DB to access.

DB.create_table :cycling do
  primary_key :id
  Float :hours
end

items = DB[:cycling] # Create a dataset

# Populate the table
5.times do
  num= Faker::Commerce.price
  items.insert(hours:  num)
end

# calling run_sql will print the results and return them so that you can test data within them.
# if you want to test different sets of data, then its best to move this code into its own top level describe
# block. If you are only testing one set though, its better to set the results before you enter a describe block
# so that the results are presented at the top of the output.
results = run_sql



describe :columns do
   it "should return 3 columns" do
    expect(results.columns.count).to eq 3
   end
end

describe :column_names do
   it "should match column names" do
    expect(results.columns[0].to_s).to eq "id"
    expect(results.columns[1].to_s).to eq "hours"
    expect(results.columns[2].to_s).to eq "liters"
   end
end

# Other tips about using run_sql:
# The SQL/code section supports multiple statements, seperated of course by a ";".
# When multiple SELECT statements are issued:
#    run_sql will return an array of arrays, unless only one SELECT statement returned results
#    INSERT and UPDATE results will not be included in the list
#    SELECT statements that return no results will not be included in the list