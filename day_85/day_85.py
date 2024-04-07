#1404. Number of Steps to Reduce a Number in Binary Representation to One
def numSteps(s):
    s = str(s)
    num = int(s, 2)
    ans = 0

    if num == 1:
        return ans

    while num != 1:
        if num % 2 == 1:
            num += 1
            ans += 1
        if num == 1:
            return ans
        num //= 2
        ans += 1

    return ans