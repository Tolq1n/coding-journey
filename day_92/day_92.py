#1221. Split a String in Balanced Strings
def balancedStringSplit(s):
    total = 0
    c = 0
    for i in range(len(s)):
        if s[i] == 'R':
            total += 1
        else:
            total -= 1
        if total == 0:
            c += 1
    return c