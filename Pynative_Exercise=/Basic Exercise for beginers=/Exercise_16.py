'''Practice Problem: 
Write a program to check if a given number is a palindrome (reads the same forwards and backwards).'''

def check_palindrome(num):
    org_num=str(num)
    reversed_num=org_num[::-1]

    if org_num == reversed_num :
        print(f"{num} is Palindrome")
        
    else:
        print(f"{num} is Not palindrome")
        
check_palindrome(121)
check_palindrome(122)

