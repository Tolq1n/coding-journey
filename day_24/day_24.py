#709. To Lower Case
def toLowerCase(s):
    lowstr = ""
    for i in s:
        if 'A' <= i <= 'Z':
            lowstr = lowstr + chr(ord(i)+32)
        else:
            lowstr = lowstr + i

    return lowstr