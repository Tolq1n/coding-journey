#1207. Unique Number of Occurrences
from collections import Counter
def uniqueOccurrences(arr):
    occurrences = {}
    for i in arr:
        if i in occurrences.keys():
            occurrences[i] += 1
        else:
            occurrences[i] = 1
    values = occurrences.values()
    return values == set(values)