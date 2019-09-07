# Title: Multiply
# Rank: 8 kyu
# Language Version: Shell bash

## Instructions ##
# The code does not execute properly. Try to figure out why.
# a=$1
# b=$2
# echo $((a*0))
#
## Solution ##
#!/bin/bash -e
a=$1
b=$2
echo $((a*b))

## Test Case ##
test1 = run_shell args: [3,4]
a=rand(0..100)
b=rand(0..100)
test2 = run_shell args: [a,b]

describe "Example Tests" do
  it "Multiple with static arguments" do
    expect(test1).to eq('12')
  end
  it "Multiply with random arguments" do
    expect(test2).to eq((a*b).to_s)
  end
end


