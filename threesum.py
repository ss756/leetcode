class Solution:
    # def threeSum(self, nums):
    #     # sorted = list(range(len(nums)))
    #     # sorted.sort(key=nums.__getitem__)
    #     nums.sort()
    #     l, r = 0, len(nums)-1
    #     result=[]
    #     while l < r:
    #         btw= nums[l+1:r]
    #         sum = nums[l] + nums[r]
    #         if sum >=0:
    #             if -sum in btw:
    #                 if [nums[l], nums[r], -sum] not in result:
    #                     result.append([nums[l], nums[r], -sum])
    #             r -= 1
    #         else:
    #             if -sum in btw:
    #                 if [nums[l], nums[r], -sum] not in result:
    #                     result.append([nums[l], nums[r], -sum])
    #             l += 1
    #     return result
    def threeSum(self, nums):
        res = []
        nums.sort()
        # check empty, all negative, all positive
        if (not nums) or nums[0] > 0 or nums[len(nums) - 1] < 0:
            return []

        for k in range(len(nums) - 2):  # beacuse two-pointer:i=k+1 and j=len(nums)-1
            if nums[k] > 0:
                break
            # skip duplicate value
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            target = 0 - nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    tmp = []
                    tmp.append(nums[k])
                    tmp.append(nums[i])
                    tmp.append(nums[j])
                    res.append(tmp)
                    # skip duplicate value
                    while (i < j and nums[i] == nums[i + 1]):
                        i = i + 1
                    while (i < j and nums[j] == nums[j - 1]):
                        j = j - 1
                    i = i + 1
                    j = j - 1
                elif nums[i] + nums[j] < target:
                    i = i + 1
                else:
                    j = j - 1

        return res





    def __init__(self):
        nums_old_example=[-1, 0, 1, 2, -1, 4]
        # nums=[-2, 0, 1, 1, 2]
        nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
        r= self.threeSum(nums)
        print(r)
Solution()











