#1450. Number of Students Doing Homework at a Given Time
def busyStudent(startTime, endTime, queryTime):
    s = 0
    for i in range(len(startTime)):
        if queryTime >= startTime[i] and endTime[i] >=queryTime:
            s += 1
    return s
    
print(busyStudent([1,2,3], [3,2,7], 4))