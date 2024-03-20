#1979. Find Greatest Common Divisor of Array
def findGCD(nums):
    nums1 = min(nums)
    nums2 = max(nums)
    for i in (range(nums1, 0, -1)):
        if nums2%i == 0 and nums1%i == 0:
            return i
