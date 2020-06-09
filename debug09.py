# class Solution:
#     def canIWin(self,  maxint: int, desiredtotal: int):
#         if maxint*(maxint+1)/2 < desiredtotal:
#             return False
#         cache = {}
#         def dp(running_total, used):
#             if used in cache:
#                 return cache[used]
#             for i in range(maxint, 0, -1):
#                 if (1 << i) & used:
#                     continue
#                 if running_total + i >= desiredtotal:
#                     cache[used] = True
#                     return True
#                 if not dp(running_total + i, (1 << i) | used):
#                     cache[used] = True
#                     return True
#             cache[used] = False
#             return False
#         return dp(0, 0)
#     def __init__(self):
#         maxint = 7
#         desiredtotal = 15
#         print(self.canIWin(maxint, desiredtotal))
# Solution()

class Solution:
    def canIwin(self, maxint: int, desiredtotal: int) -> bool:
        if maxint * (maxint + 1) < desiredtotal:
            return False
        cache= dict()
        def dp(running_total, used):
            if used in cache:
                return cache[used]
            for k in range(maxint, 0 , -1):
                if used & (1 << k):
                    continue
                if running_total + k >= desiredtotal:
                    cache[used] = True
                    return True
                if not dp(running_total + k, used | 1 << k):
                    cache[used] = True
                    return True
            cache[used] = False
            return False
        return dp(0, 0)
    def __init__(self):
            maxint = 7
            desiredtotal = 15
            print(self.canIwin(maxint, desiredtotal))
Solution()



