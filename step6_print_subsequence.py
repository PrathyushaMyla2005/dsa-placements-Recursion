def  subsequence(s,index,current):
    if index == len(s):
        print(current)
        return
    #include the current character in the subsequence
    subsequence(s,index+1,current+s[index])#we are including the current character in the subsequence and we are moving the pointer to the next character
    #exclude the current character from the subsequence
    subsequence(s,index+1,current)#we are excluding the current character from the subsequence and we are moving the pointer to the next character
s = "abc"
subsequence(s,0,"")
'''tc: O(2^n) because we are including or excluding each character in the
subsequence and we are doing this for n characters
   sc: O(n) because of the recursive call stack'''
#print_subsequence using ascill values
def sub(s,current,current_sum,index,k):
    if index == len(s):
        if current_sum == k:
            print(current)
        return
    #include the current character in the subsequence
    sub(s,index,current+s[index],current_sum+ord(s[index]))#we are including the current character in the subsequence and we are adding the ascii value of the current character to the current sum and we are moving the pointer to the next character
    #exclude the current character from the subsequence
    sub(s,index,current,current_sum,k) #we are excluding the current character from the subsequence and we are moving the pointer to the next character
s = "abc"
k = 294
sub(s,"",0,0,k)
'''tc: O(2^n) because we are including or excluding each character in the subsequence and we are doing this for n characters
   sc: O(n) because of the recursive call stack'''
#count the number of subsequences 
def count_sub(s,index):
    if index == len(s): #if we have reached the end of the string then we are returning 1 because we have found a subsequence
        return 1
    #include the current character in the subsequence
    take = count_sub(s,index+1) #we are including the current character in the subsequence and we are moving the pointer to the next character
    #exclude the current character from the subsequence
    skip = count_sub(s,index+1) #we are excluding the current character from the subsequence and we are moving the pointer to the next character
    return take + skip #we are returning the total number of subsequences by adding the number of subsequences found by including the current character and the number of subsequences found by excluding the current character
s = "abc"
print(count_sub(s,0)) #we are calling the count_sub function for the string and the starting index
'''tc: O(2^n) because we are including or excluding each character in the subsequence and we are doing this for n characters
   sc: O(n) because of the recursive call stack'''
'''Check if a String is Subsequence of Another'''
def str(s1,s2,i,j):
    if i == len(s1):#if we have reached the end of the first string then we are returning True because we have found a subsequence
        return True #if we have reached the end of the second string then we are returning False because we have not found a subsequence
    if j == len(s2): 
        return False #if the current characters of both strings are the same then we are moving the pointer of the first string to the next character and we are moving the pointer of the second string to the next character
    if s1[i] == s2[j]:
        return str(s1,s2,i+1,j+1) #if the current characters of both strings are the same then we are moving the pointer of the first string to the next character and we are moving the pointer of the second string to the next character
    #if the current characters of both strings are not the same then we are moving the pointer  
    #of the second string to the next character
    return str(s1,s2,i,j+1) #if the current characters of both
    #strings are not the same then we are moving the pointer of the second string to the next character
s1 = "abc"
s2 = "ahbgdc"
print(str(s1,s2,0,0)) #we are calling the str function for
#the two strings and the starting indices of both strings
'''tc: O(n) because we are traversing the second string once and we are checking
each character of the second string with the current character of the first string
   sc: O(n) because of the recursive call stack'''
#. Longest Subsequence Length (Recursion only)
def longest(s1,s2,i,j):
    if i == len(s1) or j == len(s2):#if we have reached the end of either string then we are returning 0 because we have not found a common subsequence
        return 0 #if the current characters of both strings are the same then we are moving the pointer of the first string to the next character and we are moving the pointer of the second string to the next character and we are adding 1 to the length of the longest subsequence found so far
    if s1[i] == s2[j]:#if the current characters of both strings are the same then we are moving the pointer of the first string to the next character and we are moving the pointer of the second string to the next character and we are adding 1 to the length of the longest subsequence found so far
        return 1 + longest(s1,s2,i+1,j+1) #if the current characters of both strings are the same then we are moving the pointer of the first string to the next character and we are moving the pointer of the second string to the next character and we are adding 1 to the length of the longest subsequence found so far
    #if the current characters of both strings are not the same then we are moving the pointer of the first string to the next character and we are keeping the pointer of the second string at the same character and we are finding the length of the longest subsequence found so far
    #by moving the pointer of the first string to the next character and keeping the pointer of
    #the second string at the same character and we are finding the length of the longest subsequence found so far by keeping the pointer of the first string at the same character and moving the pointer of the second string to the next character
    return max(longest(s1,s2,i+1,j), longest(s1,s2,i,j+1)) #if the current characters of both strings are not the same then we are moving the pointer of the first string to the next character and we are keeping the pointer of the second string at the same character and we are finding the length of the longest subsequence found so far by moving the pointer of the first string to the next character and keeping the pointer of the second string at the same character and we are finding the length of the longest subsequence found so far by keeping the pointer of the first string at the same character and moving the pointer of the second string to the next character
s1 = "abcde"
s2 = "ace"
print(longest(s1,s2,0,0)) #we are calling the longest function for the two strings and the starting indices of both strings
'''tc: O(2^n) because we are checking each character of both strings and we are doing this for n characters
   sc: O(n) because of the recursive call stack'''
#Print Unique Subsequences  with duplicates
def unique(s,index,current,result):#if we have reached the end of the string then we are adding the current subsequence to the result set and we are returning
    if index == len(s):
        result.add(current) #if we have reached the end of the string then we are adding the current subsequence to the result set and we are returning
        return #we are including the current character in the subsequence and we are moving the pointer to the next character
    unique(s,index+1,current+s[index],result) #we are including the current character in the subsequence and we are moving the pointer to the next character
    #we are excluding the current character from the subsequence and we are moving the pointer to the next character
    unique(s,index+1,current,result) #we are excluding the current character from the subsequence and we are moving the pointer to the next character
s = "aaa"
result = set() #we are creating a set to store the unique subsequences
unique(s,0,"",result) #we are calling the unique function for the string and the starting index and the empty current subsequence and the result set
print(result) #we are printing the unique subsequences
'''tc: O(2^n) because we are including or excluding each character in the subsequence and we are doing this for n characters
   sc: O(n) because of the recursive call stack'''
#Print Unique Subsequences  with duplicates using list
def unique(s,index,current,result):#if we have reached the end of the string then we are adding the current subsequence to the result set and we are returning
    if index == len(s):
        if current not in result: #if the current subsequence is not already in the result list then we are adding it to the result list
            result.append(current) #if the current subsequence is not already in the result list then we are adding it to the result list
        return #we are including the current character in the subsequence and we are moving the pointer to the next character
    unique(s,index+1,current+s[index],result) #we are including the current character in the subsequence and we are moving the pointer to the next character
    #we are excluding the current character from the subsequence and we are moving the pointer to the next character
    unique(s,index+1,current,result) #we are excluding the current character from the subsequence and we are moving the pointer to the next character