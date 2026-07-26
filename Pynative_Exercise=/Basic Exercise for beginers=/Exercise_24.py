'''Practice Problem: 
Write a program to print the first 15 terms of the Fibonacci series. 
The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.'''
t=int(input('Enter the No of Terms'))
num1,num2=0,1
for i in range(t):
    print(num1,end=' ')
    result=num1+num2
    num1=num2
    num2=result
