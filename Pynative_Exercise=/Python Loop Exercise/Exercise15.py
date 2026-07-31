'''Practice Problem: 
Write a program to find the largest and smallest digit within a given integer 
(e.g., in 75869, the largest is 9 and the smallest is 5).'''
num=758696
if num == 0:
    highest=lowest=0
else:
    highest=num%10
    lowest=num%10
    num=num//10
    while num>0:
        digit=num % 10
        if digit > highest:
            highest=digit
        if digit < lowest:
            lowest=digit
    
        num=num//10
print('highest no is',highest)
print('lowest no is',lowest)