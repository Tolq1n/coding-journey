#1528. Shuffle String
def restoreString(s, indices):
    ans = ""
    for i in range(len(indices)):
            ans += s[indices.index(i)]
    return ans