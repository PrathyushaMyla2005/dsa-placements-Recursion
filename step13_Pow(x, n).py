def power(x,n):
    if n == 0:
        return 1
    return x * power(x, n-1)

print(power(2, 3))  # Output: 8
'''tc: O(n) - The function makes n recursive calls, where n is the exponent. Each call performs a constant amount of work (multiplication), leading to a linear time complexity.
sc: O(n) - The space complexity is O(n) due to the recursive call stack. Each recursive call adds a new layer to the call stack, and in the worst case, there will be n calls on the stack before reaching the base case. Therefore, the space complexity is linear with respect to n.'''