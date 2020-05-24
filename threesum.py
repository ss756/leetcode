class Solution:
    def threeSum(self, nums):
        # sorted = list(range(len(nums)))
        # sorted.sort(key=nums.__getitem__)
        nums.sort()
        l, r = 0, len(nums)-1
        result=[]
        while l < r:
            btw= nums[l+1:r]
            sum = nums[l] + nums[r]
            if sum >=0:
                if -sum in btw:
                    if [nums[l], nums[r], -sum] not in result:
                        result.append([nums[l], nums[r], -sum])
                r -= 1
            else:
                if -sum in btw:
                    if [nums[l], nums[r], -sum] not in result:
                        result.append([nums[l], nums[r], -sum])
                l += 1
        return result
    def __init__(self):
        nums_old_example=[-1, 0, 1, 2, -1, 4]
        # nums=[-2, 0, 1, 1, 2]
        nums    = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
        r= self.threeSum(nums)
        print(r)
Solution()











