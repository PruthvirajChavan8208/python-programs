'''Practice Problem:
Write a function to return True if the first and last number of a given list is the same.
If the numbers are different, return False.'''
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def First_to_last_check(G_list):
    if G_list[-1] == G_list[0]:
        return True
    else:
        return False

print(f'For{numbers_x}:{First_to_last_check(numbers_x)}')
print(f'For{numbers_y}:{First_to_last_check(numbers_y)}')