-- Title: Register for the Party (SQL for Beginners #3)
-- Rank: 8 kyu
-- Language Version: PostgreSQL 9.6

---- Instructions ----
-- You received an invitation to an amazing party. Now you need to write an insert statement to add yourself to the table of participants.
-- participants table schema
-- name (string)
-- age (integer)
-- attending (boolean)
-- NOTES:
-- Since alcohol will be served, you can only attend if you are 21 or older
-- You can't attend if the attending column returns anything but true
-- Don't remove the 'SELECT' command from the solution!
-- Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.
--
---- Solution ----
INSERT into participants
values
    ('test' , 42, true);

SELECT *
FROM participants;

---- Test Case ----
# Run SQL
results = run_sql

# Tests
describe :participants do
   it "should return 3 participants" do
    expect
(results.count).to eq 3
end
end