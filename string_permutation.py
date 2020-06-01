def permute_string_method_one(s: str, prefix=''):
    if len(s) == 0:
        print(prefix)
        return
    for k in range(0, len(s)):
        permute_string_method_one(s[0:k]+s[k+1:], prefix + s[k])


if __name__ == "__main__":
    s = "abc"
    permute_string_method_one(s)

