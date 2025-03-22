from math import *

a = input()
temp = a

while True:
    if len(a) > 1:
        tong = 0
        for i in a:
            tong += int(i) ** 2
        a = str(tong)
    else:
        if int(a) == 0 or int(a) == 1:
            if a == "0":
                print(f"{temp} là số buồn bã")
            else:
                print(f"{temp} là số hạnh phúc")
        else:
            print(f"{temp} không buồn bã cũng không hạnh phúc")
        break