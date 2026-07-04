def bubble_sort(arr, n):
    # Base Case
    if n == 1:#if the array has only one element then it is sorted
        return#if the last element is less than the second last element then it is not sorted
    
    # One pass (largest element goes to end)
    for i in range(n-1):#we are checking each element with the next element and if the current element is greater than the next element then we are swapping them
        if arr[i] > arr[i+1]:#if the current element is greater than the next element then we are swapping them
            arr[i], arr[i+1] = arr[i+1], arr[i]#if the current element is greater than the next element then we are swapping them
    
    # Recursive call for remaining array
    bubble_sort(arr, n-1)#we are calling the bubble_sort function for the remaining array except the last element because the last element is already sorted


# Example
arr = [5, 3, 4, 1]#we are sorting the array using bubble sort
bubble_sort(arr, len(arr))#we are calling the bubble_sort function for the array and the length of the array
print(arr)#we are printing the sorted array
'''tc: O(n^2) because we are checking each element with the next element and we are doing this for n-1 elements
   sc: O(n) because of the recursive call stack'''
'''trace the example in the code  
   arr = [5, 3, 4, 1]
   n = 4
   bubble_sort(arr, n)
   #first pass
   i = 0
   arr[0] > arr[1] => 5 > 3 => True => swap => arr = [3, 5, 4, 1]
   i = 1
   arr[1] > arr[2] => 5 > 4 => True => swap => arr = [3, 4, 5, 1]
   i = 2
   arr[2] > arr[3] => 5 > 1 => True => swap => arr = [3, 4, 1, 5]
   #second pass
   i = 0
   arr[0] > arr[1] => 3 > 4 => False => no swap => arr = [3, 4, 1, 5]
   i = 1
   arr[1] > arr[2] => 4 > 1 => True => swap => arr = [3, 1, 4, 5]
   #third pass
   i = 0
   arr[0] > arr[1] => 3 > 1 => True => swap => arr = [1, 3, 4, 5]
   #fourth pass
   i = 0
   arr[0] > arr[1] => 1 > 3 => False => no swap => arr = [1, 3, 4, 5]
   #fifth pass
   i = 0
   arr[0] > arr[1] => 1 > 3 => False => no swap => arr = [1, 3, 4, 5]
   #sixth pass
   i = 0
   arr[0] > arr[1] => 1 > 3 => False => no swap => arr = [1, 3, 4, 5]
   #seventh pass
   i = 0
   arr[0] > arr[1] => 1 > 3 => False => no swap => arr = [1, 3, 4, 5]
   #eighth pass
   # we are checking the first element with the next element and we are doing this for n-1 elements
   # we are doing this for n-1 elements because the last element is '''