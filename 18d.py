import math

# 1. Định nghĩa hàm lambda kiểm tra số hoàn thiện
is_perfect = lambda n: n > 1 and (1 + sum(d + n//d if d*d != n else d for d in range(2, int(math.sqrt(n)) + 1) if n % d == 0)) == n

# 2. In các số thỏa điều kiện từ 1 đến 1 triệu
print("Các số hoàn thiện từ 1 đến 1 triệu:")
for i in range(1, 1000001):
    if is_perfect(i):
        print(i, end=" ")
print()
