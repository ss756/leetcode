class Solution:
    # two pointer method binar
    def numSubarraysWithSum1(self, A, S: int) -> int:
        A.sort()
        print(A)
        counter = 0
        if S == 0:
            for k in range(0,len(A)):
                if A[k] == 0:
                    counter +=1
        for k in range(0, len(A) - 1):
            r = len(A)
            btw = A[k + 1:r]
            target = S - A[k]
            while (k + 1) < r:
                if sum(A[k + 1:r]) == target:
                    counter += 1
                r -= 1
        return counter
    # using hashmaps
    def numSubarraysWithSum(self, A, S):
        nums = A
        cumsum, res = 0, 0
        hashmap = {0: 1}
        for x in nums:
            cumsum += x
            if cumsum - S in hashmap:
                res += hashmap[cumsum - S]
            hashmap[cumsum] = hashmap.get(cumsum, 0) + 1
        return res

    def __init__(self):
        A=[0, 1, 0, 1, 0]
        sum =2
        print(self.numSubarraysWithSum(A,sum))
Solution()