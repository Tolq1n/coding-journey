#75. Sort Colors
def sortColors(self, nums):
    n = len(nums)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if nums[j] > nums[j + 1]:
                swapped = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if not swapped:
            return