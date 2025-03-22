from math import * 

file_in = open("somayman.inp")
file_out = open("somayman.out")

s = file_in.readline()
s = s.split()
n = int(s[0])
k = int(s[1])

if 1 <= k <= n:
    count = 1
else:
    count = 0