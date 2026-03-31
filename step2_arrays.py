#sorted  using recursion
def sorted_arr(arr,n):#n is the length of the array
    if n == 1:#if the array has only one element then it is sorted
        return True#if the last element is less than the second last element then it is not sorted
    if arr[n-1] < arr[n-2]:#if the last element is less than the second last element then it is not sorted
        return False#if the last element is greater than the second last element then it is sorted
    return sorted_arr(arr,n-1)#if the last element is greater than the second last element then it is sorted
arr = [1, 2, 3, 4, 5]
n = len(arr)
print(sorted_arr(arr,n))
'''tc: O(n) because we are checking each element once
   sc: O(n) because of the recursive call stack'''
#linear search using recursion
def linear_search(arr,i,target):#i is the index of the current element we are checking and target is the element we are looking for
    if i == len(arr):#if we have reached the end of the array and we have not found the target then we return -1
        return -1#if the current element is the target then we return the index of the current element
    if arr[i] == target:#if the current element is the target then we return the index of the current element
        return i#if the current element is not the target then we check the next element
    return linear_search(arr,i+1,target)#if the current element is not the target then we check the next element
arr = [1, 2, 3, 4, 5]
target = 3
print(linear_search(arr,0,target))
'''tc: O(n) because we are checking each element once
   sc: O(n) because of the recursive call stack'''
#binarysearch using recursion
def binary_search(arr,i,low,high,key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return binary_search(arr,i,low,mid-1,key)
    return binary_search(arr,i,mid+1,high,key)
arr = [1, 2, 3, 4, 5]
key = 3
print(binary_search(arr,0,0,len(arr)-1,key))
'''tc: O(log n) because we are dividing the array into half in each step
   sc: O(log n) because of the recursive call stack'''

