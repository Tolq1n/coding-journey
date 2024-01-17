#268. Missing Number
def missingNumber(nums):
    for i in nums:
        if i-1 not in nums and i - 2 in nums:
            return i-1
            
        if i+1 not in nums and i+2 in nums:
            print(i+1)
            return i+1
    if min(nums)>=1:
        return min(nums) - 1
    else:
        return max(nums) + 1

print(missingNumber([1,2,3,4,5]))