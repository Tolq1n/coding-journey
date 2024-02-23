#2114. Maximum Number of Words Found in Sentences
def mostWordsFound(sentences):
    return max(s.count(" ") for s in sentences) + 1