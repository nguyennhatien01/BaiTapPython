# 1) Tính tổng các chữ số của n bằng đệ quy
def tong_chu_so(n):
    if n == 0:
        return 0
    return n % 10 + tong_chu_so(n // 10)


# 2) Tính giai thừa n!
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)


# 3) Tính a^b bằng đệ quy
def luy_thua(a, b):
    if b == 0:
        return 1
    return a * luy_thua(a, b - 1)


# 4) Tìm ước số chung lớn nhất (GCD)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 5) Tìm số Fibonacci thứ n
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# ==============================
# CHƯƠNG TRÌNH CHÍNH
# ==============================

# Bài 1
n = int(input("Nhập số nguyên n: "))
print("Tổng các chữ số của n =", tong_chu_so(n))

# Bài 2
n = int(input("\nNhập n để tính giai thừa: "))
print("n! =", giai_thua(n))

# Bài 3
a = int(input("\nNhập a: "))
b = int(input("Nhập b: "))
print("a^b =", luy_thua(a, b))

# Bài 4
a = int(input("\nNhập số a: "))
b = int(input("Nhập số b: "))
print("Ước chung lớn nhất =", gcd(a, b))

# Bài 5
n = int(input("\nNhập n để tìm Fibonacci: "))
print("Số Fibonacci thứ", n, "=", fibonacci(n))