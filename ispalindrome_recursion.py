def palindrome(s: str) -> bool:
    if len(s) ==1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False

if __name__ =="__main__":
    target_string = "raceca"
    print(palindrome(target_string))