class Solution:
    def divide(self, dividend, divisor):
        sum = 0
        if dividend < divisor:
            return 0
        dividend, sum = get_exp(dividend, divisor)
        print("hola", dividend, sum )
        while dividend > divisor:
            dividend, d = get_exp(dividend, divisor)
            sum +=d
            print(sum, dividend)
        if dividend == divisor:
            sum += 1
        return sum
    def __init__(self):
        dividend = 2147483648
        divisor = 2
        print(self.divide(dividend,divisor))


def get_exp(dividend, divisor):
    counter = 0
    d = divisor
    while divisor < dividend:
        counter += 1
        divisor *= d
    dividend = dividend - (d ** counter)
    return dividend, d ** (counter-1)

Solution()


