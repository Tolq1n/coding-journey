#168. Excel Sheet Column Title

def convertToTitle(columnNumber):
    """
        :type columnNumber: int
        :rtype: str
    """

    title = ''

    while columnNumber > 26:

        columnNumber -= 1

        title += chr(ord('A') + columnNumber % 26)

        columnNumber = columnNumber // 26

    columnNumber -= 1

    title += chr(ord('A') + columnNumber)

    return title[::-1]

print(convertToTitle(702))

