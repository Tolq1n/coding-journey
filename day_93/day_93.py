#1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
def findMinFibonacciNumbers(k):
    fib=[]
    f1=f2=1

    while f1<=k:
        fib.append(f1)
        temp=f1
        f1=f1+f2
        f2=temp

    total=0

    for f in fib[::-1]:
        if f<=k:
            k-=f
            total+=1

        if k==0:
            return total