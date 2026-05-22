# Kiểm tra nếu tất cả các chữ số đều nằm trong tập hợp {'6', '8'}
is_loc_phat_all = lambda n: all(char in ('6', '8') for char in str(n))

print("Số lộc phát (Cách 1 - all) từ 1 đến 1000:")
for i in range(1, 1001):
    if is_loc_phat_all(i):
        print(i, end=" ")
print("\n")
