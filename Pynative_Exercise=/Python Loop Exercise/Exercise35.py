#Practice Problem: Write a program to check if a number is a “Perfect Number.” A perfect number is a positive integer that is equal to the sum of 
#its proper divisors (excluding the number itself). For example, 6 is perfect because 1 + 2 + 3 = 6.
num=28
a=[]
for i in range(1,num//2+1):
    if num%i==0:
        a.append(i)
print(a)        
print(sum(a))        
if sum(a)==num:
    print("perfect number")
else:
    print("not a perfect no")
        