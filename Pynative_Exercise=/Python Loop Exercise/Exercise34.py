#Practice Problem: Write a program to display the Fibonacci sequence up to 10 terms. The sequence starts with 0 and 1, and each 
#subsequent number is the sum of the two preceding ones.
num1,num2=0,1
for i in range (10):
    print(num1,end=" ")
    result =num1+num2
    num1=num2
    num2=result 