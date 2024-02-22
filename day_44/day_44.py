#1470. Shuffle the Array
def shuffle(nums, n):
    i = 0
    j = n
    ans = []

    while i <= n-1:
        ans.append(nums[i])
        ans.append(nums[j])
        i += 1
        j += 1

    return ans