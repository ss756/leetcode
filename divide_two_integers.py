'''

'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend > 0 and divisor > 0 or (dividend < 0 and divisor < 0):
            sign =1
        else:
            sign = -1
        if dividend == - 2**31 and divisor == -1:
            return 2**31 - 1
        if divisor == 1:
            return dividend if sign == 1 else -dividend
        if dividend < divisor:
            return 0
        divisor = abs(divisor)
        dividend = abs(dividend)
        d = divisor
        sum = 1
        result = 0
        while True:
            if dividend > (divisor << 1):
                divisor = divisor << 1
                sum += sum
            else:
                dividend -= divisor
                result += sum
                divisor = d
                sum = 1
                if dividend < (divisor <<1 ):
                    result += 1
                    break
        return result if sign == 1 else -result
    def __init__(self):
        dividend = 31
        divisor =2
        print(self.divide(dividend, divisor))

Solution()









