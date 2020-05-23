'''
    Problem Statement:
    Given a string, find the length of the longest substring without repeating characters.


    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr:str=''
        max_length:int=0
        counter=0
        for character in s:
            if character in substr:
                substr=substr[substr.index(character)+1:]
            substr+=character
            if (len(substr)>max_length):
                max_length=len(substr)
            counter+=1
        return max_length