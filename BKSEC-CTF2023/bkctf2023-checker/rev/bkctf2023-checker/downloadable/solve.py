v3 = "BKctf2023"
v5 = v3.lower()

v6 = [
        46, 106, 119, 140, 105, 195, 195, 219, 180, 116,
        151, 68, 191, 86, 169, 205, 195, 211, 107, 120,
        110, 129, 160, 189, 189, 189, 194, 164, 102,
        110, 123, 111
    ]
v7 = [
        219, 117, 231, 96, 201, 195, 228, 201, 255,
        228, 195, 252, 219, 234, 213, 138, 138, 138,
        96, 240, 228, 207, 195, 249, 207, 96, 261,
        195, 219, 252, 99, 30
    ]
for v8 in v7:
        print(chr(v8 // 3), end="")
print()

flag = [0] * 32
flag[0] = chr(v6[0] ^ ord(v5[0]))
print()
for v9 in range(1,32):
    x = v6[v9] - ord(flag[v9-1])
    flag[v9] =  chr(x^ ord(v5[v9 % len(v5)]) )
    
print("".join(flag))