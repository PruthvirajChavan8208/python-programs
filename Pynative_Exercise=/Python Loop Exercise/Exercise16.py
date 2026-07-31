'''Practice Problem: Write a program to check if a given number is a palindrome. 
A palindrome number is a number that remains the same when its digits are reversed (e.g., 121, 343).'''
num=121
duplicate=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if duplicate == reverse:
    print('Yes Palindrome')
else:
    print('No Not palindrome')
