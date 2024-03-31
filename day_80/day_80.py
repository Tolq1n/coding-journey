#378. Kth Smallest Element in a Sorted Matrix
def kthSmallest(matrix, k):
    arr = []
    for i in range(len(matrix)):
        arr = arr + matrix[i]
    arr.sort()
    return arr[k-1]