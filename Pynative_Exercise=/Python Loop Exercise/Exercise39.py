'''Practice Problem: Given a nested list (a list containing other lists), write a program to “flatten” it into a single 
list containing all the individual elements.'''
nested_list = [[10, 20], [30, 40], [50, 60]]
# import numpy as np

# nested_list = [[10, 20], [30, 40], [50, 60]]
# arr=np.array(nested_list)
# print(arr.reshape(1,6))
flat_list=[]
for i in nested_list:
    for j in i:
        flat_list.append(j)
print(flat_list)