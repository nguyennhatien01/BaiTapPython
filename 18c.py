# Kiểm tra nếu tất cả các ký tự đều trùng với ký tự đầu tiên
is_uniform_all = lambda k: k > 0 and all(char == str(k)[0] for char in str(k))

print("Số đồng nhất (Cách 1 - all):")
for i in range(1, 1000001):
    if is_uniform_all(i):
        print(i, end=" ")
print("\n")
