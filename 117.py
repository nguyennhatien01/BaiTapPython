n = input("Nhap n: ")

tong = 0

for i in range(len(n)):

    for j in range(i + 1, len(n) + 1):

        sub = n[i:j]

        so = int(sub)

        tong += so ** 2

print("Tong S =", tong)