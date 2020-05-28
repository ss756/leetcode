class Solution:
    def manacher(self, s:str):
        manachar_list = self.preprocess(s)
        lps = [0] * len(manachar_list)
        center = 0
        right = 0
        for i in range(1, len(lps)-1):
            mirror = 2 * center - i
            if right > i:
                lps[i] = min(right - i, lps[mirror])
            while manachar_list[i+(1+lps[i])] == manachar_list[i - (1+lps[i])]:
                lps[i] += 1
            if i + lps[i] > right:
                center = i
                right = lps[i]+ center
        return manachar_list, lps

    def longestPalindromicSubstring(self, lps) -> str:
        print(original_string)
        length = 0
        center = 0
        for k in range(1,len(lps)-1):
            if lps[k] > length:
                length = lps[k]
                center = k
        start = int((center - 1 - length)/2)
        end = int((center - 1 + length)/2)
        return original_string[start:end]

    def longestpalindromesubstring(self, lps, i: int):
        length = lps[i+2]
        center = i+2
        return original_string[int((center-1-length)/2):int((center-1+length)/2)]



    def preprocess(self, s:str):
        t = [""]*(2*len(s)+3)
        t[0] = "$"
        t[2*len(s)+2] = "@"
        for i in range(0, len(s)):
            t[2*i +1] ="#"
            t[2*i+2] = s[i]
        t[2*len(s)+1] = "#"
        return t


    def __init__(self):
        global original_string
        original_string= "aabaaad"
        manacher_list, lps = (self.manacher(original_string))
        longest_palindrome= self.longestPalindromicSubstring(lps)
        print("LONGEST PALINDROME IS", longest_palindrome)
        for i in range(0,2*len(original_string)):
            print(i, ":", self.longestpalindromesubstring(lps,i))
Solution()



