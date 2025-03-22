from math import *

a = 0
while a <= 0:
    a = int(input("Nhập vào số nguyên a: "))
    if a <= 0:
        print("Vui lòng nhập lại a, điều kiện là a > 0")

b = a
while b <= a:
    b = int(input("Nhập vào số nguyên b: "))
    if b <= a:
        print("Vui lòng nhập lại b, điều kiện là b > a")

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

tong = 0
s = ""
for i in range(a, b + 1):
    if nguyento(i):
        tong += i
    if i % 5 == 0:
        s = s + str(i) + " "

print(f"Tổng của các số nguyên tố trong khoảng từ {a} đến {b} là {tong}")
print(f"Các số chia hết cho 5 trong dãy số từ {a} đến {b} là {s}")
