'''Practice Problem: Given a dictionary of student scores, create a new dictionary that only includes 
students who scored above a certain threshold (e.g., 75).'''
scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60} 
threshold = 75
b={}
for name,marks in scores.items():
    if marks > threshold:
        b[name]=marks
print(b)

