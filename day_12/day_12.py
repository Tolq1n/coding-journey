#13. Roman to Integer
def romanToInt(s):
    a={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    }

    # print(s)
    t = 0

    for i in range(len(s)):
        if i < len(s) - 1 and a[s[i]] < a[s[i+1]]:
            t -= a[s[i]]
        else:
            t += a[s[i]]
    print(t)
    return t
romanToInt('XLIX')