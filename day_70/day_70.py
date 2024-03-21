#476. Number Complement
def findComplement(num):
    com = ''
    while num > 0 :

        if num % 2 == 1:
            com += '0'
        else:
            com += '1'
        num = num // 2
    print(com)
    return int(com[::-1],2)