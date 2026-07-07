'''unique paths
example:
Input: m = 3, n = 2
Output: 3   '''
class Solution:
    def uniquePaths(self, m, n):

        def dfs(i, j):

            # Base Case 1: Reached destination
            if i == m - 1 and j == n - 1:
                return 1

            # Base Case 2: Outside the grid
            if i >= m or j >= n:
                return 0

            # Go Right
            right = dfs(i, j + 1)

            # Go Down
            down = dfs(i + 1, j)

            # Total ways
            return right + down

        return dfs(0, 0)
    
    