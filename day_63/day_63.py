#260. Single Number III
from collections import Counter
def singleNumber(nums):
        ans = []
        if len(nums) <= 2:
             return nums
        for i, j in Counter(nums).items():
            print('i', i, 'j', j)
            if j == 1:
                ans.append(i)
        return ans