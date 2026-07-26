'''Practice Problem:
 Write a program to extract each digit from an integer in the reverse order.'''

# Method 1
# number = 7536
# r_num=str(number)
# reverse_num=r_num[::-1]

# print(reverse_num)
# Method 2
number = 7536
reverse=0
while number > 0:
    digits=number%10
    reverse=reverse*10+digits
    
    number=number//10
print(reverse,end=" ")
