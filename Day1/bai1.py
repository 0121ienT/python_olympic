from math import *

file_in = open("root.inp")
file_out = open("root.out", "w")

a = int(file_in.readline())
b = int(file_in.readline())
c = int(file_in.readline())

tu = a**2 + b**2 + c**2
mau = a * b * c

result = tu / mau + sqrt(mau)

result = str(round(result, 2))

file_out.write(result)

print(result)

file_in.close()
file_out.close()
