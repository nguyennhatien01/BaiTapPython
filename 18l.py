# Kết hợp điều kiện: chỉ chứa 6 và 8 (dùng cách 1) VÀ chuỗi viết xuôi bằng chuỗi viết ngược
is_loc_phat_palindrome = lambda n: all(char in ('6', '8') for char in str(n)) and str(n) == str(n)[::-1]

print("Các số lộc phát Palindrome từ 1 đến 1 triệu:")
for i in range(1, 1000001):
    if is_loc_phat_palindrome(i):
        print(i, end=" ")
print()
