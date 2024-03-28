#1502. Can Make Arithmetic Progression From Sequence
def canMakeArithmeticProgression(self, arr):
    arr.sort()
    delta = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != delta:
            return False
    return True