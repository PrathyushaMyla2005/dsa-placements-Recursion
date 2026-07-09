class Solution(object):
    def rob(self,nums):
        n = len(nums)
        def helper(i):
            # Base Case 1: Reached the end of the list
            if i >= n:
                return 0
            rob = nums[i] + helper(i + 2)  # Rob the current house and skip the next one
            skip = helper(i + 1)  # Skip the current house and move to the next one
            return max(rob, skip)  # Return the maximum of robbing or skipping
        return helper(0)  # Start from the first house
nums = [1, 2, 3, 1]
solution = Solution()
result = solution.rob(nums)
'''tc: O(2^n) - Exponential time complexity due to the recursive calls for each house.
sc: O(n) - The maximum depth of the recursion stack can go up to n in
the worst case.'''