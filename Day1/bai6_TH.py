a = int(input())

s = ""
tong = 0

for i in range(1, a):
    if a  % i == 0:
        s += str(i) + " "
        tong += i

if tong == a:
    print(f"Đây là số hoàn hảo có các ước là {s}")
else:
    print("Không phải số hoàn hảo")