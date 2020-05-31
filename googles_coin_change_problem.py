def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    if s == target:
        print("sum {} is {}".format(partial, target))
    if s >= target:
        return
    for i in range(0, len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        print(n,remaining, partial)
        subset_sum(remaining, target, [n] + partial)

if __name__ == "__main__":
    numbers= [3, 5, 7, 9, 8, 12]
    target = 20
    subset_sum(numbers, target)

