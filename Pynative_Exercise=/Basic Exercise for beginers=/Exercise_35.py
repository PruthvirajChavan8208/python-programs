'''Practice Problem: 
Write a program to check if a user-entered string contains any numeric digits. 
Use a for loop to examine each character.'''
input_string = "Python4"
num_contain=False
for i in input_string:
    if i.isdigit():
        num_contain=True
        break
print(f'{input_string} has digits:{num_contain}')