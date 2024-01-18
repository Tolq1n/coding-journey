#1281. Subtract the Product and Sum of Digits of an Integer
def subtractProductAndSum(n):
    s=0
    q=1
    while n!=0: 
        s+=n%10
        q*=n%10
        n//=10
    return q-s

subtractProductAndSum(1)