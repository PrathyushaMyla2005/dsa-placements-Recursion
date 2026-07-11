def binary_search(nums, target, left, right):

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        return binary_search(nums, target, mid + 1, right)

    else:
        return binary_search(nums, target, left, mid - 1)


# Driver code
nums = [-1, 0, 3, 5, 9, 12]
target = 9

result = binary_search(nums, target, 0, len(nums) - 1)
print(result)

'''tc: O(log n) - The search space is halved with each recursive call.
sc: O(log n) - The maximum depth of the recursion stack can go up to log'''