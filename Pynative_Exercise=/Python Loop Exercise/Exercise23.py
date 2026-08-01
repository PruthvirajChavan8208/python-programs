#Practice Problem: Write a program to print a triangle pattern where each row consists of the same letter, and the letter changes (increments)
# with each new row.
Ascii_values=65
num=5
for i in range(5):
    letter = chr(Ascii_values+i)
    for j in range(i+1):
        print(letter,end="")
    print ("\n")   