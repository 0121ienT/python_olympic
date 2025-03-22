from math import *

file_in = open("toanco.inp")
file_out = open("toanco.out", "w")

s = file_in.readline()

s = s.split(" ")

m, n= int(s[0]), int(s[1])

a = b = 0
for a in range(m):
    b = m - a
    if 2 * a + 4 * b == n:
        break

file_out.write(str(a) + " " + str(b))
file_in.close()
file_out.close()