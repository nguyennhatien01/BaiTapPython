import math

# 1. Định nghĩa hàm lambda kiểm tra số thân thiện
is_friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# 2. In các số thỏa điều kiện từ 1 đến 1 triệu (Ví dụ in 20 số đầu tiên để test)
print("Các số thân thiện đầu tiên:")
count = 0
for i in range(1, 1000001):
    if is_friendly(i):
        print(i, end=" ")
        count += 1
        if count >= 20:  # Giới hạn in để tránh tràn màn hình
            break
print("\n")
