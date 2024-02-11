#349. Intersection of Two Arrays
def intersection(nums1, nums2):
    ans = []
    for num in nums1:
        if num in nums2 and num not in ans:
            ans.append(num)

    return ans
