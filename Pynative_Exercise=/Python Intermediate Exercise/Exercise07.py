#Practice Problem: Write a function to check if a full sentence 
#is a palindrome. You must ignore case, spaces, and all punctuation marks.
text="A man, a plan, a canal: Panama"
def reverse_palindrome(sentence):
    new_char=[word.lower() for word in sentence if word.isalnum()]
    new_str="".join(new_char)
    print(new_str)
    if new_str == new_str[::-1]:
        return True 
    
result =reverse_palindrome(text)   
print(f"the result for: {text} is :{result}")