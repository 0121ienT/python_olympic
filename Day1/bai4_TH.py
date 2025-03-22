from math import *

file_in = open("bl2.inp")
file_out = open("bl2.out", "w")

s = file_in.read()

s = s.split()

c = int(s[0])
t = int(s[1])
A = int(s[2])
k = float(s[3])
h = float(s[4])

if c == 0:
    total = A
    for i in range(t):
        total = total + total * (h / 100)
    file_out.write(str(round(total,1)))
else:
    if t < c:
        total = A
        for i in range(t):
            total = total + total * (h / 100)
        file_out.write(str(round(total,1)))
    else:
        total = A
        for i in range(t):
            if i + 1 <= c:
                total = total + total * (k / 100)
            else:
                total = total + total * (h / 100)
        file_out.write(str(round(total, 1)))