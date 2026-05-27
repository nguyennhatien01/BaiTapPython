import math

# Định nghĩa giới hạn quét dữ liệu từ 1 đến 1 triệu theo yêu cầu đề bài
MAX_LIMIT = 1000000

# ==============================================================================
# BƯỚC CHUẨN BỊ: SÀNG SỐ NGUYÊN TỐ ERATOSTHENES (Dành cho câu j)
# Tạo trước mảng đánh dấu để các hàm lambda truy xuất nhanh O(1), tránh tạo hàm phụ
# ==============================================================================
is_prime_list = [True] * (MAX_LIMIT + 1)
is_prime_list[0] = is_prime_list[1] = False  # 0 và 1 không phải số nguyên tố

for i in range(2, int(math.sqrt(MAX_LIMIT)) + 1):
    if is_prime_list[i]:
        for j in range(i * i, MAX_LIMIT + 1, i):
            is_prime_list[j] = False


# ==============================================================================
# ĐỊNH NGHĨA TẤT CẢ CÁC HÀM ẨN DANH (LAMBDA FUNCTIONS) TỪ A ĐẾN L
# ==============================================================================

# a) Số thân thiện: Ước chung lớn nhất của n và số đảo ngược của n bằng 1
is_friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# b) Số chính phương: Bình phương phần nguyên căn bậc hai của n phải bằng chính nó
is_perfect_square = lambda n: int(math.sqrt(n)) ** 2 == n

# c) Số đồng nhất (Cách 1): Sử dụng hàm all() để kiểm tra mọi ký tự giống ký tự đầu
is_identical_all = lambda n: all(char == str(n)[0] for char in str(n))

# c) Số đồng nhất (Cách 2): Sử dụng hàm any() kiểm tra không có ký tự nào khác ký tự đầu
is_identical_any = lambda n: not any(char != str(n)[0] for char in str(n))

# d) Số hoàn thiện: Tổng các ước số thực sự (duyệt đến một nửa n để tối ưu) bằng chính nó
is_perfect_number = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

# e) Số phong phú: Tổng các ước số thực sự (không kể n) lớn hơn chính nó
is_abundant = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) > n

# f) Số tăng dần: Mọi cặp chữ số liên tiếp đều thỏa mãn ký tự trước <= ký tự sau
is_increasing = lambda n: all(str(n)[i] <= str(n)[i+1] for i in range(len(str(n)) - 1))

# g) Số Armstrong: Tổng các chữ số sau khi lũy thừa với số bậc (chiều dài chuỗi) bằng chính nó
is_armstrong = lambda n: sum(int(char) ** len(str(n)) for char in str(n)) == n

# i) Số Palindrome: Chuỗi ký tự đọc xuôi hay đọc ngược ([::-1]) đều trùng nhau
is_palindrome = lambda n: str(n) == str(n)[::-1]

# j) Số nguyên tố Palindrome: Truy xuất mảng sàng nguyên tố phối hợp với logic đảo chuỗi đối xứng
is_prime_palindrome = lambda n: is_prime_list[n] and str(n) == str(n)[::-1]

# k) Số lộc phát (Cách 1): Sử dụng hàm all() để chắc chắn các ký tự nằm trong ['6', '8']
is_lucky_all = lambda n: all(char in ['6', '8'] for char in str(n))

# k) Số lộc phát (Cách 2): Tổng số lượng ký tự '6' và '8' phải bằng đúng chiều dài chuỗi số
is_lucky_count = lambda n: str(n).count('6') + str(n).count('8') == len(str(n))

# l) Số lộc phát Palindrome: Thỏa mãn đồng thời điều kiện lộc phát (all) và tính đối xứng
is_lucky_palindrome = lambda n: all(char in ['6', '8'] for char in str(n)) and str(n) == str(n)[::-1]


# ==============================================================================
# HÀM MAIN - ĐIỀU KHIỂN LOGIC RA MÀN HÌNH CONSOLE
# ==============================================================================
def main():
    print(f"=== CHƯƠNG TRÌNH KIỂM TRA CÁC LOẠI SỐ TỪ 1 ĐẾN {MAX_LIMIT} ===")
    
    # Do tập dữ liệu 1 triệu phần tử rất lớn, một số câu nhiều kết quả sẽ được giới hạn số lượng in mẫu.
    
    # --- CÂU A ---
    print("\na) Các số thân thiện (In mẫu 30 số đầu tiên):")
    count = 0
    for i in range(1, MAX_LIMIT + 1):
        if is_friendly(i):
            print(i, end=" ")
            count += 1
            if count >= 30: break
            
    # --- CÂU B ---
    print("\n\nb) Các số chính phương:")
    for i in range(1, MAX_LIMIT + 1):
        if is_perfect_square(i):
            print(i, end=" ")
            
    # --- CÂU C (CÁCH 1) ---
    print("\n\nc) Số đồng nhất (Cách 1 - dùng all()):")
    for i in range(1, MAX_LIMIT + 1):
        if is_identical_all(i):
            print(i, end=" ")
            
    # --- CÂU C (CÁCH 2) ---
    print("\n\nc) Số đồng nhất (Cách 2 - dùng any()):")
    for i in range(1, MAX_LIMIT + 1):
        if is_identical_any(i):
            print(i, end=" ")
            
    # --- CÂU D ---
    print("\n\nd) Các số hoàn thiện:")
    for i in range(1, MAX_LIMIT + 1):
        if is_perfect_number(i):
            print(i, end=" ")
            
    # --- CÂU E ---
    print("\n\ne) Các số phong phú (In mẫu 40 số đầu tiên):")
    count = 0
    for i in range(1, MAX_LIMIT + 1):
        if is_abundant(i):
            print(i, end=" ")
            count += 1
            if count >= 40: break
            
    # --- CÂU F ---
    print("\n\nf) Các số tăng dần (In mẫu 30 số đầu tiên):")
    count = 0
    for i in range(1, MAX_LIMIT + 1):
        if is_increasing(i):
            print(i, end=" ")
            count += 1
            if count >= 30: break
            
    # --- CÂU G ---
    print("\n\ng) Các số Armstrong:")
    for i in range(1, MAX_LIMIT + 1):
        if is_armstrong(i):
            print(i, end=" ")
            
    # --- CÂU I ---
    print("\n\ni) Các số Palindrome (In mẫu 30 số đầu tiên):")
    count = 0
    for i in range(1, MAX_LIMIT + 1):
        if is_palindrome(i):
            print(i, end=" ")
            count += 1
            if count >= 30: break
            
    # --- CÂU J ---
    print("\n\nj) Các số nguyên tố Palindrome dưới 20000 (Để đối chiếu mẫu đề bài):")
    for i in range(1, 20000):
        if is_prime_palindrome(i):
            print(i, end=" ")
            
    # --- CÂU K (CÁCH 1) ---
    print("\n\nk) Các số lộc phát (Cách 1 - dùng all()):")
    for i in range(1, MAX_LIMIT + 1):
        if is_lucky_all(i):
            print(i, end=" ")
            
    # --- CÂU K (CÁCH 2) ---
    print("\n\nk) Các số lộc phát (Cách 2 - dùng count()):")
    for i in range(1, MAX_LIMIT + 1):
        if is_lucky_count(i):
            print(i, end=" ")
            
    # --- CÂU L ---
    print("\n\nl) Các số lộc phát Palindrome:")
    for i in range(1, MAX_LIMIT + 1):
        if is_lucky_palindrome(i):
            print(i, end=" ")
    print("\n")

if __name__ == "__main__":
    main()
