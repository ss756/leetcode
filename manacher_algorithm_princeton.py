class Solution:
    def manacher(self, s:str):
        manachar_list = self.preprocess(s)
        print(manachar_list)
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
            print(i,manachar_list[i], center,right, lps[i], mirror)









    def preprocess(self, s:str) -> str:
        t = [""]*(2*len(s)+3)
        t[0] = "$"
        t[2*len(s)+2] = "@"
        for i in range(0, len(s)):
            t[2*i +1] ="#"
            t[2*i+2] = s[i]
        t[2*len(s)+1] = "#"
        return t


    def __init__(self):
        original_string="aabaaad"
        (self.manacher(original_string))


Solution()



