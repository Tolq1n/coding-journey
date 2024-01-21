#2000. Reverse Prefix of Word
def reversePrefix(word, ch):
    if ch not in word:
        return word

    l = len(ch)
    i = word.index(ch)
    return word[:i+l][::-1] + word[i+l:]


print(reversePrefix("salom", 'o'))
