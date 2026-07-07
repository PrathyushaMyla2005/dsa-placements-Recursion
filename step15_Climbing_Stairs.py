def climbStairs(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

        # Recursive Formula
        return climbStairs(n - 1) + climbStairs(n - 2)
n = 5
print(climbStairs(n))  # Output: 8