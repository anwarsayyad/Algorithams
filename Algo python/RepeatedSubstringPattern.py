def repeatedSubstringPattern(s):
    n = len(s)
    for i in range(1, n//2 + 1):
        if n % i == 0:
            substring = s[:i]
            if substring * (n//i) == s:
                return True
    return False

def repeatedStringPattern2(s):
    return s in (s+s)[1:-1]

print(repeatedSubstringPattern('abab'))