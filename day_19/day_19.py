#1295. Find Numbers with Even Number of Digits
def findNumbers(nums):
    return sum(len(str(n)) % 2 == 0 for n in nums)