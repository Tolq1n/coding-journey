def merge(nums1, m, nums2, n):
    ans = nums1[:m] + nums2[:n]
    ans.sort()
    return ans
print(merge([0], 0, [1], 1))
