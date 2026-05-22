import math

# 1. Định nghĩa hàm lambda kiểm tra số nguyên tố Palindrome
# Điều kiện: n > 1 VÀ n là Palindrome VÀ n không chia hết cho số nào từ 2 đến căn bậc hai của n
is_prime_palindrome = lambda n: n > 1 and str(n) == str(n)[::-1] and not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))

# 2. In các số nguyên tố Palindrome dưới 20000 để đối chiếu với ví dụ trong đề
print("Các số nguyên tố Palindrome dưới 20000:")
for i in range(1, 20001):
    if is_prime_palindrome(i):
        print(i, end=" ")
print()
