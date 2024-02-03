#2778. Sum of Squares of Special Elements
def sumOfSquares(nums):

    n=len(nums)
    s=0

    for i in range(n):
        if n%(i+1)==0:
            s=s+nums[i]**2
    return s

print(sumOfSquares([2,7,1,19,18,3]))