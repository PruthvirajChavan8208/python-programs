'''Practice Problem: 
Write a program to use a loop to find the factorial of a given number 
(e.g., 5!). The factorial of N is the product of all integers from 1 to N.'''
num=5
fact=1
if num <0:
    print('Cant determine')
if num ==0:
    print('Factorial of 0 is 1')
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print(f'factorial of {num} is:{fact}')