'''Practice Problem: 
Write a program to reverse a given integer number (e.g., 76542 should become 24567).'''
num=76542
reverse=0
while num >0:
    digits=num % 10
    reverse=reverse*10+digits
    num=num//10
print(reverse)