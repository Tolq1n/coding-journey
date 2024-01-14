#2520. Count the Digits That Divide a Number
def countDigits(num):
    s=0
    duplicate = num
    while num != 0:
        q = num % 10
        if q != 0 and duplicate % q == 0:
            s += 1
        num //= 10
    return s

print(countDigits(107))