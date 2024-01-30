#2119. A Number After a Double Reversal
def isSameAfterReversals(num):
    if num==0:
        return True
    elif num %10==0:
        return False
    else:
        return True

isSameAfterReversals(12)