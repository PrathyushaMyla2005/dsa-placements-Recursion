#print to 1 to 5 num using recursion 
'''def nums(n):
    if n == 0:
        return 
    nums(n-1)
    print(n)
n = 5
print(nums(n))
def nums(n):
    if n == 5:
        return
    print(n)
    nums(n+1)
n = 5
print(nums(n))
#fibonacci series
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
n = 10
print(fib(n))
#binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    return binary_search(arr, target, mid + 1, end)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
#factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
n = 5
print(f"Factorial of {n} is {factorial(n)}")
#sum of digits of a number
def sum_of_digits(n):
    if n == 0:
        return 0
    rem = n % 10
    n = n // 10
    return rem + sum_of_digits(n)
n = 12345
print(f"Sum of digits of {n} is {sum_of_digits(n)}")'''
#reverse a string
def reverse_string(n):
    if len(s) == 0:
        return s
    rem = n % 10
    rev = rev * 10 + rem
    return reverse_string(n // 10)
s = "Hello, World!"
print(f"Reversed string: {reverse_string(s)}")
#palindrome string
def is_palindrome(s):
    if  n == reverse_string(s):
        return True
    return False
s = "madam"
if is_palindrome(s):
    print(f"{s} is a palindrome.")
else:    print(f"{s} is not a palindrome.")
#count the zeros in a number
def count_zeros(n):
    if n == 0:
        return 1
    if n < 10:
        return 0
    rem = n % 10
    count = count_zeros(n // 10)
    if rem == 0:
        count += 1
    return count
n = 1002003
print(f"Number of zeros in {n} is {count_zeros(n)}")

