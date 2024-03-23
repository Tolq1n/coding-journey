#1859. Sorting the Sentence
def sortSentence(s):
    a = s[::-1].split()
    a.sort()
    r = []

    for word in a:
        r.append(word[1:][::-1])

    return " ".join(r)