'''Practice Problem: Write a program to print the following pattern using nested loops:'''
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print('\n')

for k in range(4,0,-1):
    for l in range(k):
        print('*',end='')
    print('\n')
