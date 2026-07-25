'''Practice Problem: 
Write a script that takes a list containing duplicate items and returns a new list with only unique elements.'''
#method 1
data = [1, 2, 2, 3, 4, 4, 4, 5]
unique=[]
for i in data:
    if i not in unique:
        unique.append(i)

# print(f'The Unique list is:{unique}')
#method 2
# data = [1, 2, 2, 3, 4, 4, 4, 5]
# print(list(set(data)))
