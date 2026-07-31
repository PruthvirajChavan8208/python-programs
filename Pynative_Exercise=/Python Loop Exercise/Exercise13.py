'''Practice Problem: 
Write a program to count the total number of digits in a given integer using a while loop.'''
#Method 1
num=75869
# count=len(str(num))
# print(f'count of the {num} is:{count}')
#Method 2
count=0
while num>0:
    num=num//10
    count+=1
print(f'count is:{count}')
