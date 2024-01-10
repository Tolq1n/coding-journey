# 171. Excel Sheet Column Number


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        i = len(columnTitle) - 1
        s = 0
        for letter in columnTitle:
            s += (ord(letter)-64)*26**i
            i -= 1
        return s