#2427. Number of Common Factors
def commonFactors(a, b):
    s=0
    if a > b:
        for i in range(1, a+1):
            if a%i == 0 and b%i == 0:
                print('a>b', i)
                s+=1
    else:
        for i in range(1, b+1):
            if a%i == 0 and b%i == 0:
                print('b>a', i)
                s+=1
    return s