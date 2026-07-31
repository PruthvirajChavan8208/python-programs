#Practice Problem: Write a program that counts the total number of vowels and consonants in a 
#given sentence, ignoring spaces and special characters.
text="Loops are Fun!"
vowels=["a","e","i","o","u"]
v_count=0
c_count=0
for i in text.lower():
    if i.isalpha():
        if i in vowels:
            v_count+=1
        else :
            c_count+=1
print(f"the {text} has")       
print(f"vowels:{v_count}")   
print(f"constants:{c_count}")
