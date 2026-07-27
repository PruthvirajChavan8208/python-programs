'''Practice Problem: 
Take two lists and find the elements that appear in both. Use Sets to perform the operation.'''
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
a=[]
for i in list_a:
    for j in list_b:
        if i == j:
            a.append(i)
print(set(a))