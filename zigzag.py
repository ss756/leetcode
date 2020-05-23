'''
    Problem Statement:
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I
'''


# approach number one (execution time is not good this can be optimised)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row=1
        character_pos= list(range(len(s)))
        final_str=''
        for i in range(0, len(s)):
            if numRows == 1:
                return s
            if row == numRows:
                down_movement = False
            elif row == 1:
                down_movement = True
            if down_movement == True:
                character_pos[i]=row
                row+=1
            if down_movement == False:
                character_pos[i]=row
                row-=1
        for i in range(1,numRows+1):
            row_str=''
            for j in range(len(character_pos)):
                if character_pos[j]==i:
                    row_str+= s[j]
            final_str+=row_str
            row_str=''
        return final_str

# second approach (A better approach)
class Solution():
    def convert(self, s: str, numRows: int):
        if numRows == 1:
            return s
        period: int = 2 * (numRows - 1)
        dictionary = dict()
        lines = ["" for i in range(numRows)]
        for i in range(0, len(s)):
            if i < numRows:
                dictionary[i] = i
            else:
                dictionary[i] = period - i
        for i in range(len(s)):
            lines[dictionary[i % period]] += s[i]
        return "".join(lines)
    def __init__(self):
        str="PAYPALISHIRING"
        result= self.convert(self,str,4)
        print(result)
