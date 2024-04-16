#2149. Rearrange Array Elements by Sign
def rearrangeArray(nums):
    positive=[]
    negative=[]
    for num in nums:
        if num<0:
            negative.append(num)
        else:
            positive.append(num)
    ans=[]
    for p,n in zip(positive,negative):
        ans.append(p)
        ans.append(n)
    return ans