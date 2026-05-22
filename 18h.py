#cách 1: Đếm số ước của n, nếu có đúng 2 ước là 1 và chính nó thì n là số nguyên tố
# Đếm xem có bao nhiêu số từ 1 đến n mà n chia hết, nếu bằng 2 thì là số nguyên tố
#is_prime_c1 = lambda n: sum(1 for i in range(1, n + 1) if n % i == 0) == 2

#print("Cách 1 - Số nguyên tố đầu tiên:")
#for i in range(1, 100):
#    if is_prime_c1(i):
#        print(i, end=" ")
#print("\n")



# Cách 2: Sử dụng hàm all để kiểm tra nếu n chia hết cho bất kỳ số nào từ 2 đến căn bậc hai của n   
# Tính tổng tất cả các ước, nếu tổng bằng n + 1 thì là số nguyên tố
is_prime_c2 = lambda n: sum(i for i in range(1, n + 1) if n % i == 0) == n + 1

print("Cách 2 - Số nguyên tố đầu tiên:")
for i in range(1, 100):
    if is_prime_c2(i):
        print(i, end=" ")
print("\n")
