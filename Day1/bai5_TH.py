from math import *

file_in = open("nt.inp")
file_out = open("nt.out", "w")

n = file_in.readline()
n = int(n)

def nguyento(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
    return True

while n:
    a = file_in.readline()
    a = int(a)
    for i in range(a - 1):
        if nguyento(i) and nguyento(a - i):
            break
    file_out.writelines(f"{str(a)} = {str(i)} + {int(a) - i}\n")
    n -= 1

file_in.close()
file_out.close()