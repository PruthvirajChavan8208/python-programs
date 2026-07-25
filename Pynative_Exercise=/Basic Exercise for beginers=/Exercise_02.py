'''Practice Problem: 
Iterate through the first 10 numbers (0–9). In each iteration, print the current number,
the previous number, and their sum.'''
prev_no=0
for i in range(0,10):

    print(f'Current Number {i} Previous Number {prev_no} Sum: {i+(prev_no)}')
    prev_no=i
 
