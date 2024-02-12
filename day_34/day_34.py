#169. Majority Element
def majorityElement(self, nums):
    nums.sort()
    return nums[len(nums) // 2]
