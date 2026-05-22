import math

# 1. Định nghĩa hàm lambda kiểm tra số phong phú (sử dụng tối ưu căn bậc hai)
is_abundant = lambda n: n > 1 and (1 + sum(d + n//d if d*d != n else d for d in range(2, int(math.sqrt(n)) + 1) if n % d == 0)) > n

# 2. In các số thỏa điều kiện từ 1 đến 1 triệu (Ví dụ in các số < 100 giống đề bài)
print("Các số phong phú nhỏ hơn 100:")
for i in range(1, 101):
    if is_abundant(i):
        print(i, end=" ")
print("\n")
