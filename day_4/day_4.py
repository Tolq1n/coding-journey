#70. Climbing Stairs
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        f0 = 1
        f1 = 1
        total = 0

        for i in range(1, n):
            total = f0 + f1
            f0 = f1
            f1 = total
        return total

print(climbStairs(45))