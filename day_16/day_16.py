#2942. Find Words Containing Character
def findWordsContaining(words, x):
    res = []
    for i, word in enumerate(words):
        if x in word:
            res.append(i)
    return res