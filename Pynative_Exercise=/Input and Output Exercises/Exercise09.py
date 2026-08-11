#Practice Problem: Ask the user for a word and a number. Print the word right-aligned in a total field width of 20 characters, 
#followed by the number.
num=int(input("Enter the number"))
str=input ("enter the word")
print(f"{str:>20}:{num}")