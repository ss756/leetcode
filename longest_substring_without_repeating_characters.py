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