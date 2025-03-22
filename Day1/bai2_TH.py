from math import *

def ucln(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    if b == 0:
        return 
    while b:
        a, b = b, a % b
    return a

ps = input()

a, b = ps.split("/")

uoc_chung = ucln(int(a), int(b))

print(f"{int(int(a) / uoc_chung)}/{int(int(b) / uoc_chung)}")