'''Practice Problem: 
Create a countdown timer that starts from a given number and counts down to zero using a while loop.'''
import time
n=int(input("Enter the timer starts count"))

while n>=0:
    print(n)
    time.sleep(1)
    n-=1
    if n == 0:
        print('Blast Off')
        break