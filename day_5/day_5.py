# 728. Self Dividing Numbers
def selfDividingNumbers(left, right):

    def selfDividing(x, duplicate):
        if '0' in x:
            return False
        for num in x:
            if duplicate % int(num) != 0:
                return False
        return True

    a = []
    for i in range(left, right+1):
        duplicate = i
        if selfDividing(str(i), duplicate):
            a.append(i)
    return a

print(selfDividingNumbers(1, 10000))