#1662. Check If Two String Arrays are Equivalent
def arrayStringsAreEqual(word1, word2):
    first_word1 = "".join(word1)
    second_word2 = "".join(word2)
    return True if first_word1==second_word2 else False