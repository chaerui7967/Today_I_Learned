# 난이도 초급

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]

# =====다른방법
class Solution:
    def twoSum(self, nums, target):
        vals = []
        for i in range(len(nums)):
            if nums[i] in vals:
                return [vals.index(nums[i]), i]
            vals.append(target - nums[i])