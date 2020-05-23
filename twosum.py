'''
Problem statement:
    Given an array of integers return indices of the two numbers such that they add to a specific number
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].

'''

# approach number one

class Solution:
    def twoSum(self, nums, target :int):
        computed_sum={}
        for i,e in enumerate(nums):
            if (target-e) in computed_sum: return [computed_sum[target-e],i]
            computed_sum[e]=i
        return []

# approach number two
class Solution:
    def twoSum(self,nums,target):
        newList=list(range(len(nums)))
        newList.sort(key=nums.__getitem__)
        lhs,rhs= 0, len(nums)-1
        while lhs < rhs:
            sum= nums[newList[lhs]]+nums[newList[rhs]]
            if sum == target:
                return [newList[lhs],newList[rhs]]
            elif sum>target:
                rhs-=1
            else :
                lhs+=1
        return []