#Practice Problem: Write a function that determines if two strings are anagrams 
#(contain the exact same characters in a different order).
word1 = "listen"
word2 = "silent"
def is_anagram(s1,s2):
    str1=sorted(s1.lower())
    str2=sorted(s2.lower())
    return str1==str2
    
result =is_anagram(word1,word2)    
print(f"{word1} and {word2} is: anagram?{result}")
        