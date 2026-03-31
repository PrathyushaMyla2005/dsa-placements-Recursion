def selection_sort(arr,i,n):#i is the index of the current element we are checking and n is the length of the array
    if  i == n:#if we have reached the end of the array then we return
        return#if we have reached the end of the array then we return
    min_index =i#we are assuming that the current element is the minimum element and we are checking the next elements to find the minimum element
    for j in range(i+1,n):#we are checking the next elements to find the minimum element
        if arr[j] < arr[min_index]:#if the current element is less than the minimum element then we are updating the minimum element
            min_index = j#if the current element is less than the minimum element then we are updating the minimum element
    arr[i],arr[min_index] = arr[min_index],arr[i]#we are swapping the current element with the minimum element
    selection_sort(arr,i+1,n)#we are calling the selection_sort function for the next element because the current element is already sorted
arr = [5, 3, 4, 1]
i = 0
n = len(arr)
print(selection_sort(arr,i,n))
print(arr)
'''tc: O(n^2) because we are checking each element with the next element and    
we are doing this for n-1 elements
   sc: O(n) because of the recursive call stack'''