#Generate All Permutations of String
from itertools import permutations
import string


def permute(s,current):
    if len(s) == 0:#if the length of the string is 0 then we are printing the current permutation because we have found a permutation
        print(current) #if the length of the string is 0 then we are printing the current permutation because we have found a permutation
        return #we are iterating through each character in the string and we are including that character in the current permutation and we are finding the permutations of the remaining characters in the string
    for i in range(len(s)):#we are iterating through each character in the string and we are including that character in the current permutation and we are finding the permutations of the remaining characters in the string
        ch = s[i]   #we are including the current character in the current permutation and we are finding the permutations of the remaining characters in the string    
        remaining = s[:i] + s[i+1:] #we are including the current character in the current permutation and we are finding the permutations of the remaining characters in the string
        permute(remaining,current+ch) #we are including the current character in the current permutation and we are finding the permutations of the remaining characters in the string
s = "abc"
permute(s,"") #we are calling the permute function for the string and the empty current permutation
'''tc: O(n! * n) because we are generating n! permutations and for each
permutation we are concatenating the characters to form the permutation which takes O(n) time
   sc: O(n) because of the recursive call stack and the current permutation string which can be at most n characters long'''
#with duplicates
def permute(s,current,result,used,ch):
    if len(s) == 0:#if the length of the string is 0 then we are printing the current permutation because we have found a permutation
        print(current)#if the length of the string is 0 then we are printing the current permutation because we have found a permutation
        result.add(current)#if the length of the string is 0 then we are printing the current permutation because we have found a permutation and we are adding it to the result set to avoid duplicates
        return
    for i in range(len(s)):#we are iterating through each character in the string and we are including that character in the current permutation and we are finding the permutations of the remaining characters in the string
        if s[ch] in used: #if the current character is already used in the current permutation then we are skipping it to avoid duplicates
            continue #if the current character is already used in the current permutation then we are skipping it to avoid duplicates
        used.add(s[ch]) #if the current character is not already used in the current permutation then we are adding it to the used set to avoid duplicates
        remaining = s[:i] + s[i+1:] #we are including the current character in the current permutation and we are finding the permutations of the remaining characters in the string
        permute(remaining,current+s[ch],result,used,i) #we are including the
#current character in thecurrent permutation and we are finding the permutations of the remaining characters in the string
str = "aabc"
result = set() #we are creating a set to store the unique permutations
permute(str,"",result,set(),0) #we are calling the permute function for the string and the empty current permutation and the result set and the used set and the starting index
'''tc: O(n! * n) because we are generating n! permutations and for each
permutation we are concatenating the characters to form the permutation which takes O(n) time and
we are using a set to avoid duplicates which takes O(1) time for each insertion
   sc: O(n) because of the recursive call stack and the current permutation string which can be at most n characters long and the used set which can have at most n characters'''
