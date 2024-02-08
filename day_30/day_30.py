#2788. Split Strings by Separator
def splitWordsBySeparator(words, separator):
    ans = []
    for word in words:
        s = ""
        for i, char in enumerate(word):
            if char != separator:
                s += char
            else:
                if s:
                    ans.append(s)
                    s = ""
        if s:
            ans.append(s)

    return ans