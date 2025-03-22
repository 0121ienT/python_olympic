from math import *

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

s = ''
n = 2

while n <= 1000:
    for i in range(2,n):
        if n % i == 0 and n % (i * i) == 0:
            if nguyento(i):
                s =  s + str(n) + " "
                break
    n += 1

print(f"Các số mạnh mẽ nhỏ hơn 1000 là {s}")