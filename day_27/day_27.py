#1512. Number of Good Pairs
def numIdenticalPairs(nums):
        nums.sort()
        count=0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    count+=1
                else:
                    break
        return count