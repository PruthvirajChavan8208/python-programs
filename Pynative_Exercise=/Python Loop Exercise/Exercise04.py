'''Practice Problem: 
Write a program that accepts a number from the user and calculates the sum of all numbers 
from 1 up to that number.'''
n=int(input("Enter the number"))
s=0
for i in range(1,n+1):
    s=s+i
print(f'Sum from 1 to {n} is:{s}')

