# Title: 1. Two Sum
# Difficulty: Easy
# Language: Python3

## Problem ##
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
## Solution ##


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = 0
        for i in nums:
            k += 1
            if target - i in nums[k:]:
                return [k - 1, nums[k:].index(target - i) + k]

# My first attempt, failed due to time limit exceeding
# issue was solution used 2 loops
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] + nums[j] == target and i != j:
#             return [i, j]

# This being the first problem, and labeled easy ain't no joke
