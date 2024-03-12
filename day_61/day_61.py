#451. Sort Characters By Frequency
def frequencySort(s):
    frequency = {}
    for i in s:
        if i in frequency.keys():
            frequency[i] += 1
        else:
            frequency[i] = 1
    sorted_keys = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
    ans = ''
    for key in sorted_keys:
            ans += key * frequency[key]
    return ans