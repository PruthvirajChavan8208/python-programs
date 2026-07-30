'''Practice Problem: Given a list, iterate it in reverse order and print each element.'''
list1 = [10, 20, 30, 40, 50]
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])
#method 2
for i in reversed(list1):
    print(i)