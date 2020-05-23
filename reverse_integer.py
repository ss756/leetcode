'''
PROBLEM STATEMENT:
    Given a 32-bit signed integer, reverse digits of an integer.
    Remember the reversed string should in this limit  [2**31 -1 , -2 **31 ]
'''

class Solution:
        #     def reverse(self, x: int) -> int:
        #         result = 0
        #         abs_x = abs(x)
        #         while abs_x != 0 :
        #             remainder = abs_x % 10
        #             abs_x = abs_x //10

        #             temp = result * 10 + remainder
        #             result = temp

        #         if x < 0 :
        #             result = -1 * result

        #         if result < - 2**31 or result > 2**31 -1:
        #             result = 0

        #         return result
        def reverse(self, x: int) -> int:
            absx = str(abs(x))
            reversed = int(absx[::-1])
            if x < 0:
                reversed *= -1
            if reversed > 2 ** 31 - 1 or reversed < -2 ** 31:
                return 0
            return reversed

        def __init__(self):
                print(self.reverse(15342364969))

Solution()