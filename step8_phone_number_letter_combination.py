def letter(digits):#letter combinations of a phone number
    if digits == " ":#if the input is empty then we are returning an empty string because there are no combinations of letters for an empty input
        return [""]#if the input is empty then we are returning an empty string because there are no combinations of letters for an empty input
    phone = {
        2 : "abc",#if the digit is 2 then we are returning the letters "abc" because these are the letters corresponding to the digit 2 on a phone keypad
        3 : "def",#if the digit is 3 then we are returning the letters "def" because these are the letters corresponding to the digit 3 on a phone keypad
        4 : "ghi",#if the digit is 4 then we are returning the letters "ghi" because these are the letters corresponding to the digit 4 on a phone keypad
        5 : "jkl",#if the digit is 5 then we are returning the letters "jkl" because these are the letters corresponding to the digit 5 on a phone keypad
        6 : "mno",#if the digit is 6 then we are returning the letters "mno" because these are the letters corresponding to the digit 6 on a phone keypad
        7 : "pqrs",#if the digit is 7 then we are returning the letters "pqrs" because these are the letters corresponding to the digit 7 on a phone keypad
        8 : "tuv",#if the digit is 8 then we are returning the letters "tuv" because these are the letters corresponding to the digit 8 on a phone keypad
        9 : "wxyz"

    }
    result = []#we are creating a list to store the combinations of letters for the given digits
    def backtrack(index,current):#we are using backtracking to generate all combinations of letters for the given digits
        if index == len(digits):#if we have reached the end of the digits then we are adding the current combination of letters to the result list because we have found a valid combination of letters for the given digits
            result.append(current)#if we have reached the end of the digits then we are adding the current combination of letters to the result list because we have found a valid combination of letters for the given digits
            return#if we have reached the end of the digits then we are adding the current combination of letters to the result list because we have found a valid combination of letters for the given digits
        digit = digits[index]#we are getting the current digit from the input digits string and we are finding the corresponding letters for that digit from the phone dictionary
        letters = phone[digit]#we are getting the corresponding letters for the current digit from the phone dictionary
        for i in range (len(letters)):#we are iterating through the letters corresponding to the current digit and we are including each letter in the current combination and we are finding the combinations of letters for the remaining digits
            backtrack(index+1,current+letters[i])#we are including the current letter in the current combination and we are finding the combinations of letters for the remaining digits by moving the pointer to the next digit and adding the current letter to the current combination
        backtrack(0,"")#we are calling the backtrack function for the starting index and the empty current combination
        return result#we are returning the result list which contains all combinations of letters for the given digits
digits = "23"
print(letter(digits))
'''tc: O(4^n) because each digit can have at most 4 letters and we are generating all combinations of letters for the given digits
   sc: O(n) because of the recursive call stack and the current combination string which can be at most n characters long'''