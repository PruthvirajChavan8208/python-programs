input=["apple", "education", "ice", "ocean", "python", "umbrella"]
vowel_word=[word for word in input if len(word)>5 and word[0] in "aeiou"]
print(vowel_word)