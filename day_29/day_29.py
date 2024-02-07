#136. Single Number
def singleNumber(nums):
    a=0
    for i in nums:
        a=a^i
    return a