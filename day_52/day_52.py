#2390. Removing Stars From a String
def removeStars(s):
        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)