import string
from random import *

def finalstage(w):
    h = 0
    w = list(w)
    w.reverse()
    flag = 'flag'.replace('flag', 'galf').replace('galf', '')
    while h < len(w):
        try:
            flag += w[h+1] + w[h]
        except:
            flag += w[h]
        h+=2
    print("Final Stage complete")
    return flag

def stage2(b):
    t = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++.++++++.-----------.++++++."[-15:(7*9)].strip('-')
    print("t = "+ t)
    for q in range(len(b)):
        t += chr(ord(b[q])-randint(0,5))
    print("Stage 2 complete")
    flag = finalstage(t)
    return flag

def stage1(a):
    a = list(a)
    b = list(string.ascii_lowercase)
    for o in range(len(a)):
        a[o] = chr(ord(a[o])^o)
    z = "".join(x for x in a)
    for y in range(len(z)):
        b[y%len(b)] = chr((ord(z[y])^ord(a[y]))+len(b))
    print("Stage 1 complete")
    flag = stage2(z)
    return flag
    
def entry(f):
    seed(10)
    f = list(f) 
    f.reverse() 
    f = "".join(i for i in f)
    print("Entry complete")
    flag = stage1(f)
    return flag 

flag = open('output.txt', 'r').readlines()[0]
print(len(flag))
input = entry(input("Enter Flag: "))
if input == flag:
    print("win")
else:
    print("NOOOOOOOOOOOOOOO")