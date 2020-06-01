def power(x: int, n: int):
    if n ==0:
        return 1
    else:
        return x*power(x, n-1)

def power9(x: int, n: int):
    if n == 0:
        return 1
    else:
        if n % 2 ==1:
            return x*power9(x, n-1)
        else:
            y = power(x, int(n/2))
            return y*y
if __name__ == "__main__":
    print("Recursive power", power(4,3))
    print("Recursive Optimized power", power9(4,4))




