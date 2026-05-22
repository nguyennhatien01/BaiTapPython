# 1. Định nghĩa hàm lambda kiểm tra số Armstrong
# Lấy độ dài chuỗi làm số mũ, tính tổng lũy thừa từng chữ số rồi so sánh với số ban đầu
is_armstrong = lambda n: sum(int(digit) ** len(str(n)) for digit in str(n)) == n

# 2. In các số thỏa điều kiện từ 1 đến 1 triệu
print("Các số Armstrong từ 1 đến 1 triệu:")
for i in range(1, 1000001):
    if is_armstrong(i):
        print(i, end=" ")
print()
