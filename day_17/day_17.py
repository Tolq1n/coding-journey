#2535. Difference Between Element Sum and Digit Sum of an Array
def differenceOfSum(nums):
    sum1 = sum(nums)
    sum2 = 0
    for num in nums:
        for j in str(num):
            sum2 += int(j)
    return abs(sum1 - sum2)