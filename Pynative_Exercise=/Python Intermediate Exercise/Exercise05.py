# Practice Problem: Write a recursive function that takes a list containing other lists (of any depth) and 
# returns a single “flat” list of all elements.
nested = [1, [2, 3], [4, [5, 6]], 7]
def flatten(val):
    flat_lst=[]
    for i in val:
        if isinstance(i,list):
            flat_lst.extend(flatten(i))
        else:
            flat_lst.append(i)
    return flat_lst
print(flatten(nested))


 