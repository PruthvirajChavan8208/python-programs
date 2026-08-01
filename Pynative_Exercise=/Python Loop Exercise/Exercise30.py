'''Practice Problem: Write a program to remove all duplicate values from a list using a loop, 
maintaining the original order of elements.'''
a=[1, 2, 2, 3, 4, 4, 4, 5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)