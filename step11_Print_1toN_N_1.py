'''1 to n
1, 2, 3, ..., n
n to 1
n, n-1, n-2, ..., 1,5,4,3,2,1'''
def print_1toN(n):
    if n == 0:
        return 
    print(n)
    print_1toN(n-1)
print_1toN(5)
def print_Nto1(n):
    if n == 0:
        return 
    print_Nto1(n-1)
    print(n)
print_Nto1(5)


