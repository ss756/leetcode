class Solution:
    def decodestring(self, s: str) -> str:
        stack = []
        curnum = 0
        curstr = ''
        for k in s:
            if k.isdigit():
                curnum = curnum * 10 + int(k)
            elif k == '[':
                stack.append(curstr)
                stack.append(curnum)
                curnum = 0
                curstr = ''
            elif k == ']':
                num = stack.pop()
                prevstring = stack.pop()
                curstr = prevstring + curstr * num
            else:
                curstr += k
        return curstr

    def __init__(self):
        s = "3[a2[c]]"
        print(self.decodestring(s))


Solution()
