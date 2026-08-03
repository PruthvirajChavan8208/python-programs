'''Practice Problem: Given a 2D list (matrix), find the row and column index of a target value'''
matrix = [[10, 20], [30, 40], [50, 60]]
target = 30
for r_idx,row in enumerate(matrix):
    for c_idx,val in enumerate(row):
        # print(r_idx,c_idx)
        if val == target:
            print(f'Target found in {r_idx} and {c_idx}')
