def permute_string_method_one(s: str, prefix=''):
    print("prefix", prefix)
    if len(s) == 0:
        print(prefix)
        return
    for k in range(0, len(s)):
        permute_string_method_one(s[0:k] + s[k + 1:], prefix + s[k])


def toString(a):
    return ''.join(a)


def permute_string_method_two(s, l: int, r: int):
    if l == r:
        print(toString(s))
        return
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            print(i, l, s)
            permute_string_method_two(s, l + 1, r)
            s[l], s[i] = s[i], s[l]


if __name__ == "__main__":
    s = "abcde"
    permute_string_method_one(s)
    string = "abc"
    n = len(string)
    a = list(string)
    #permute_string_method_two(a, 0, n - 1)
