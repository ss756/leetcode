'''
    Problem Statement: Given a string s find the longest palindromic substring in s.
    Input "babad"
    Output: bab
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
                result = ''
                if len(s)==1:
                    return s
                for k in range(0, len(s) - 1):
                    right = len(s)
                    while right > k:
                        sub = s[k:right]
                        reversal = sub[::-1]
                        if sub == reversal and len(sub) > len(result):
                            result = sub
                        right -= 1
                return result
    def __init__(self):
        print(self.longestPalindrome("cbbd"))

Solution()
