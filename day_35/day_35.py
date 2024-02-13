#2108. Find First Palindromic String in the Array
def firstPalindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""