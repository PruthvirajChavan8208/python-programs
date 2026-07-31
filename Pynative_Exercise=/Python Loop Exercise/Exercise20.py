'''Practice Problem: 
Write a program to print a right-angled triangle pattern where each row contains 
increasing numbers up to the row number.'''
num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end='')
    print('\n')