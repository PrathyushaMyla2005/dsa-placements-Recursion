def bubble_sort(arr, n):
    # Base Case
    if n == 1:
        return
    
    # One pass (largest element goes to end)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    # Recursive call for remaining array
    bubble_sort(arr, n-1)


# Example
arr = [5, 3, 4, 1]
bubble_sort(arr, len(arr))
print(arr)