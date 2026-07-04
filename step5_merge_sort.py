def merge_sort(arr):#if the length of the array is less than or equal to 1 then we return the array because it is already sorted
    if len(arr) <= 1:#if the length of the array is less than or equal to 1 then we return the array because it is already sorted
        return arr#we are dividing the array into two halves and we are calling the merge_sort function for both halves
    mid = len(arr) // 2#we are finding the middle index of the array and we are dividing the array into two halves
    left = arr[:mid]#we are dividing the array into two halves and we are calling the merge_sort function for both halves
    right = arr[mid:]#we are dividing the array into two halves and we are calling the merge_sort function for both halves
    left = merge_sort(left)#we are calling the merge_sort function for the left half of the array
    right = merge_sort(right)#we are calling the merge_sort function for the right half of the array 
    i = 0#we are merging the two halves of the array and we are storing the sorted elements in a new array
    j = 0#we are merging the two halves of the array and we are storing the sorted elements in a new array
    result = []#we are merging the two halves of the array and we are storing the sorted elements in a new array 
    while i < len(left) and j < len(right):#we are merging the two halves of the array and we are storing the sorted elements in a new array
        if left[i] < right[j]:#if the current element of the left half is less than the current element of the right half then we are adding the current element of the left half to the result array and we are moving the pointer of the left half to the next element
            result.append(left[i])#if the current element of the left half is less than the current element of the right half then we are adding the current element of the left half to the result array and we are moving the pointer of the left half to the next element
            i += 1#we are moving the pointer of the left half to the next element
        else:#if the current element of the right half is less than or equal to the current element of the left half then we are adding the current element of the right half to the result array and we are moving the pointer of the right half to the next element
            result.append(right[j])#if the current element of the right half is less than or equal to the current element of the left half then we are adding the current element of the right half to the result array and we are moving the pointer of the right half to the next element
            j += 1#we are moving the pointer of the right half to the next element
    while i < len(left):#if there are still elements in the left half then we are adding them to the result array
        result.append(left[i])#if there are still elements in the left half then we are adding them to the result array
        i += 1 #we are moving the pointer of the left half to the next element
    while j < len(right):#if there are still elements in the right half then we are adding them to the result array
        result.append(right[j])#if there are still elements in the right half then we are adding them to the result array
        j += 1#we are moving the pointer of the right half to the next element
    return result#we are returning the sorted array
arr = [5, 3, 4, 1]
sorted_arr = merge_sort(arr)
print(sorted_arr)
'''tc: O(n log n) because we are dividing the array into two halves and we are doing this log n times and we are merging the two halves in O(n) time
   sc: O(n) because we are creating a new array to store the sorted elements'''