# 1. Biến đổi số thành chuỗi, kiểm tra ký tự sau lớn hơn hoặc bằng ký tự trước bằng hàm all
is_increasing = lambda n: all(str(n)[i] <= str(n)[i+1] for i in range(len(str(n)) - 1))

# 2. In các số thỏa điều kiện từ 1 đến 1 triệu (Ví dụ in 30 số đầu tiên)
print("Các số tăng dần đầu tiên:")
count = 0
for i in range(1, 1000001):
    if is_increasing(i):
        print(i, end=" ")
        count += 1
        if count >= 30:
            break
print("\n")
