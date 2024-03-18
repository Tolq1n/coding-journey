#387. First Unique Character in a String
from  collections  import Counter
def firstUniqChar(s):
    cnt = Counter(s)
    print(cnt)
    for i,c in enumerate(s):
        if cnt[c]==1:
            return i
    return -1
#2351. First Letter to Appear Twice
def repeatedCharacter(s):
    arr = []
    for letter in s:
        if letter in arr:
            return letter
        arr.append(letter)