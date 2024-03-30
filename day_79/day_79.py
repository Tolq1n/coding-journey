#1351. Count Negative Numbers in a Sorted Matrix
def countNegatives(grid):
    ans = 0
    for arr in grid:
        for num in arr:
            if num < 0:
                ans += 1
    return ans