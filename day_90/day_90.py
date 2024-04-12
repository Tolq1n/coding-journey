#1732. Find the Highest Altitude
def largestAltitude(gain):
    highest_point = 0
    prev_altitude = 0
    for i in gain:
        prev_altitude += i
        highest_point = max(highest_point, prev_altitude)

    return highest_point