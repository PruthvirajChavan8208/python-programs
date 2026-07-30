'''Practice Problem: 
Create a program that takes an integer and prints its multiplication table from 1 to 10.'''
# Table
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end='\t')
#     print('\n')
num=int(input("Enter the number"))
for i in range(1,11):
    mul_table=num*i
    print(mul_table,end='\t')