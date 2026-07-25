'''Practice Problem: 
Given a list of integers, find and print both the largest and the smallest numbers.'''
# Method 1
# import numpy as np
# nums = [45, 2, 89, 12, 7]
# a=np.array(nums)
# print(f'The largest NO is:{a.max()}')
# print(f'The Smallest NO is:{a.min()}')
# Mehod 2
nums = [45, 2, 89, 12, 7]
largest=max(nums)
smallest=min(nums)

print(f'Largest No is:{largest}')
print(f'Smallest No is:{smallest}')
