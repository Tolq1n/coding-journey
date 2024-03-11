#3065. Minimum Operations to Exceed Threshold Value I
def minOperations(nums, k):
    smallest_nums=[]
    for i in nums:
        if i<k:
            smallest_nums.append(i)
    return len(smallest_nums)