#557. Reverse Words in a String III
def reverseWords(s):
    s=s.split(' ')
    ans = ''
    for i in s:
        if i == 1:
            ans+=i[::-1]
        else:
            ans+=' '+i[::-1]
    return ans
