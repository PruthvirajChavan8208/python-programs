'''Practice Problem: Given two lists, find the elements that appear in both. 
Do not use Python’s built-in set().intersection() method.'''
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
all=[]
comman=[]
for i in list_a:
    if i not in all:
        all.append(i)
    
for j in list_b:
    if j not in all:
        all.append(j)
    else:
        comman.append(j)
print(f'The comman values in both list is:{comman}')