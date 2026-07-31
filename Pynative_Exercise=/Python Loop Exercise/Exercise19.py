'''Practice Problem: 
Write a program to check if a number is an Armstrong number. An Armstrong number 
(for a 3-digit number) is an integer such that the sum of the cubes of its digits is equal to 
the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).'''
num=153
num_str=str(num)
power=len(num_str)
total=0

for i in num_str:
    total=total+int(i)**power
if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is Not an Armstrong number")
