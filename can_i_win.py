class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        cache = {}
        def dp(cur, used):
            if used in cache:
                return cache[used]

            # Iteration start from high to 1 to accelerate computation
            for i in range(maxChoosableInteger, 0, -1):
                if used & (1 << i):
                    continue
                if cur + i >= desiredTotal:
                    cache[used] = True
                    return True
                if not dp(cur + i, used | (1 << i)):
                    cache[used] = True
                    return True
            cache[used] = False
            return False
        return dp(0, 0)
    def __init__(self):
        maxchoosableInteger  =10
        desiredTotal = 11
        print(self.canIWin(maxchoosableInteger, desiredTotal))


Solution()