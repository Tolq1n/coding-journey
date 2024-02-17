#1002. Find Common Characters
def commonChars(words):
    check = list(words[0])
    for word in words:
        new_list = []
        for letter in word:
            if letter in check:
                new_list.append(letter)
                check.remove(letter)
        check = new_list

    return check