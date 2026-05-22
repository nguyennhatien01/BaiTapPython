import math

# 1. Định nghĩa hàm lambda kiểm tra số chính phương
is_square = lambda n: math.isqrt(n) ** 2 == n

# 2. In các số thỏa điều kiện từ 1 đến 1 triệu (Ví dụ in 20 số đầu tiên)
print("Các số chính phương đầu tiên:")
count = 0
for i in range(1, 1000001):
    if is_square(i):
        print(i, end=" ")
        count += 1
        if count >= 20:
            break
print("\n")
