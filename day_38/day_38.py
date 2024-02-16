#2442. Count Number of Distinct Integers After Reverse Operations
def countDistinctIntegers(nums):
    new_nums=nums[:]
    for i in nums:
        i = str(i)[::-1]
        i = int(i)
        new_nums.append(i)
    return len(list(set(new_nums)))