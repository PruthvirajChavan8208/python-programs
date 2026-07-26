'''Practice Problem: 
Write a program to check if a given number is a palindrome. 
A palindrome number remains the same when its digits are reversed (e.g., 121, 545).'''

def palindrome(num):
    str_num=str(num)
    reverse_num=str_num[::-1]

    if str_num == reverse_num :
        print(f'{num} is Palindrome')
    else:
        print(f'{num} is not Palindrome')
palindrome(121)
palindrome(545)
palindrome(67)