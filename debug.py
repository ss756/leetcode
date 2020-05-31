def allsum(numbers, target, partial=[]):
    if sum(partial) == target:
        print("{} sum is {}".format(partial, target))
    if sum(partial) > target:
        return
    for k in range(0, len(numbers)):
        n = numbers[k]
        remaining = numbers[k + 1:]
        allsum(remaining, target, [n] + partial)


if __name__ == "__main__":
    numbers = [3, 5, 7, 9, 12, -1, -5, 14, 25]
    target = 20
    allsum(numbers, target)
