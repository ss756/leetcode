from collections import defaultdict

class Solution:
    def findDuplicateone(self, nums):
        dict_map = defaultdict(lambda:x)
        result = []
        for k in nums:
            if k not in dict_map:
                dict_map[k] =0
            else:
                result.append(k)
        return result

    def __init__(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        print(self.findDuplicateone(nums))

Solution()


