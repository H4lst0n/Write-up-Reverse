def check(v2, v3):
    v4 = True
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
    
    if len(v2) != 32:
        v4 = False
    
    for v8 in v7:
        print(chr(v8 // 3), end="")
    print()
    
    for v9 in range(len(v2)):
        v10 = ord(v2[v9]) ^ ord(v5[(v9 - 1) % len(v5)])
        if v9 > 0:
            v10 = v10 + ord(v2[v9 - 1])
        if v6[v9] != v10:
            v4 = False
    
    return v4
