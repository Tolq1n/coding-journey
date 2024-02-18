#2011. Final Value of Variable After Performing Operations
def finalValueAfterOperations(operations):
    s = 0
    for i in operations:
        if "+" in i:
            s = s + 1
        else:
            s = s - 1
    return s