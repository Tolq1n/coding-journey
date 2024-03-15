#28. Find the Index of the First Occurrence in a String
def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    x = len(needle)
    for i in range(len(haystack)):
        if needle == haystack[i:i+x]:
            return i