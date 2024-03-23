#442. Find All Duplicates in an Array
def findDuplicates(nums):
    twice=[]
    once={}
    for i in range(len(nums)):
        if nums[i] in once:
            twice.append(nums[i])
        once[nums[i]]=False
    return twice