from math import *

file_in = open("input.inp")
file_out = open("output.out", "w")

n = int(file_in.readline())
s = file_in.readline()

s = s.split()
kq = 0
num = 1

while True:
    for i in range(0,n):
        temp = int(s[i])
        if (num**2) % temp != 0:
            break
    
    if i == n - 1 and (num ** 2) % temp == 0:
        kq = num ** 2 % (10**9 + 7)
        file_out.write(str(kq))
        break
    else:
        num += 1

file_in.close()
file_out.close()