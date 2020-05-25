# Awesome solution

class Solution:
    def threeSum3(self, nums):
        import collections
        res = []
        c = collections.Counter(nums)  # count the value appear time
        # Counter({-1: 2, 0: 1, 1: 1, 2: 1, -4: 1})

        import itertools
        for u, v in itertools.combinations_with_replacement(c, 2):
            # print(u,v)
            w = -u - v

            flag = False
            if w not in c:
                continue
            elif u == v == w:
                flag = c[u] > 2  # at least 3 duplicate value
            elif u == v:
                flag = c[u] > 1  # at least 2 duplicate value
            elif u < w and v < w:  # no duplicate value
                flag = True

            if flag:
                res.append([u, v, w])
        return res
    def __init__(self):
        nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
        print(self.threeSum3(nums))
Solution()