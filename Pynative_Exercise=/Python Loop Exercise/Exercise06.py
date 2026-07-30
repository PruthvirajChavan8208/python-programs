'''Practice Problem: 
Write a program that takes an integer n and prints the cube of every number from 1 to n in the 
format Current Number is : 1 and the cube is 1.'''
num=int(input("Enter The number"))
for i in range(1,num+1):
    cube=i**3
    print(f'The number is{i} and Its cube is:{cube}')