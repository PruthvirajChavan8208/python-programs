'''Practice Problem: Manually convert a binary string (e.g., "1101") into its decimal integer equivalent using a loop. 
Do not use int(binary, 2).'''
binary_str = "1101"
sum=0
reversed_str=binary_str[::-1]
for i in range(len(reversed_str)):
    if reversed_str[i] == '1':
       
        sum+=2 ** i
print(sum)