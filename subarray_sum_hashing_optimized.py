# from collections import defaultdict
# def subarray_sum(nums, target: int) ->int:
#     total = 0
#     prevsum = defaultdict(lambda: 0)
#     sum =0
#     for k in nums:
#         sum += k
#         if sum == target:
#             total +=1
#         if sum - target in prevsum:
#             total += prevsum[sum - target]
#         prevsum[sum] += 1
#     return total
#
#
# if __name__ == "__main__":
#     nums =[3, 6, -10, 7, 10, 3, 1, 2]
#     target =3
#     print(subarray_sum(nums,3))
from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        carrsum = 0
        counter = 0
        prevsum = defaultdict(lambda: 0)
        for i in nums:
            carrsum += i
            if carrsum == k:
                counter += 1
            if carrsum - k in prevsum:
                counter += prevsum[carrsum - k]
            prevsum[carrsum] += 1
        return counter
    def __init__(self):
        nums =[3, 4, 7, 2, -3, 1, 4, 2]
        target =7
        print(self.subarraySum(nums, target))

Solution()





