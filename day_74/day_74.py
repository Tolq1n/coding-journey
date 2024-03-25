#350. Intersection of Two Arrays II
from collections import Counter
def intersect(self, nums1, nums2):
    counts = Counter(nums1)
    ans = []

    for num in nums2:
        if counts[num] > 0:
            ans += num,
            counts[num] -= 1
    return ans