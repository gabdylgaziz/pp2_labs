s = input()

def palindrome(s) -> bool:
    if s[::-1] == s[::1]:
        return True
    return False
    
print(palindrome(s))