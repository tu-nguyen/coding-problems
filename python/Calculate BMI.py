# Title: Calculate BMI
# Rank: 8 kyu 
# Language Version: Python 3.4.3

## Instructions ##
# Write function bmi that calculates body mass index (bmi = weight / height ^ 2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"
# 
## Solution ##
def bmi(weight, height):
    ind = weight / height ** 2
    
    if ind <= 18.5:
        return "Underweight"
    elif ind <= 25:
        return "Normal"
    elif ind <= 30:
        return "Overweight"
    elif ind > 30:
        return "Obese"

## Test Case ##
Test.describe("Basic tests")
Test.assert_equals(bmi(50, 1.80), "Underweight")
Test.assert_equals(bmi(80, 1.80), "Normal")
Test.assert_equals(bmi(90, 1.80), "Overweight")
Test.assert_equals(bmi(110, 1.80), "Obese")
Test.assert_equals(bmi(50, 1.50), "Normal")
