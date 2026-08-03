'''Practice Problem: Manually convert a binary string (e.g., "1101") into its decimal integer equivalent using a loop. 
Do not use int(binary, 2).'''
binary_str = "1101"
binary_str = "1101"
decimal_val = 0

reversed_binary = binary_str[::-1]

for i in range(len(reversed_binary)):
    if reversed_binary[i] == '1':
        decimal_val += 2 ** i

print("Decimal value:", decimal_val)