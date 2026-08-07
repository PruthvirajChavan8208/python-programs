#Practice Problem: Create a function rotate_list(lst, n, direction) that shifts the elements of a 
# list by N positions. The direction can be ‘left’ or ‘right’.
def rotate_list(lst, n, direction='right'):
    if not lst:
        return lst
    n = n % len(lst)
    if direction == 'right':
        return lst[-n:] + lst[:-n]
    else:
        return lst[n:] + lst[:n]

data = [1, 2, 3, 4, 5]
print(rotate_list(data,2,'right'))
print(rotate_list(data,2,'left'))