#2418. Sort the People
def sortPeople(names, heights):
    data = {heights[i]:names[i] for i in range(len(names))}
    return [data[i] for i in sorted(data, reverse = True)]