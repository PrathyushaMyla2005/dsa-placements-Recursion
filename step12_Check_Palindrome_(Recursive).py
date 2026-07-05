def is_palindrome(s, start, end):
    # Base case: If the start index is greater than or equal to the end index, it's a palindrome
    if start >= end:
        return True
    
    # Check if the characters at the start and end indices are the same
    if s[start] != s[end]:
        return False
    
    # Recursive case: Move towards the center of the string
    return is_palindrome(s, start + 1, end - 1)
word = "racecar"
print(is_palindrome(word, 0, len(word) - 1))  # Output: True
