#1047. Remove All Adjacent Duplicates In String
def removeDuplicates(s):
    ans=[]
    for x in s:
        if len(ans)>0 and ans[-1]==x:
            ans.pop()
        else:
            ans.append(x)
    return ''.join(ans)