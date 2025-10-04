"""
Write a function which check whether a word is 
palindrome or not.
"""

word = input("Enter a word: ")

def IsPalindrome(a):
    if a == a[::-1]:
        return "Is palindrom"
    return "not palindrome"

print(IsPalindrome(word))