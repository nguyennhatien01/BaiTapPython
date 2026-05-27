import math

# ==============================================================================
# HÀM BỔ TRỢ: KIỂM TRA SỐ NGUYÊN TỐ (Tối ưu hóa với độ phức tạp O(sqrt(n)))
# Được sử dụng lại xuyên suốt trong các bài 2, 3, 4, 5 để tránh lặp mã nguồn
# ==============================================================================
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Duyệt bước nhảy 6 để tối ưu hóa kiểm tra các số dạng 6k +/- 1
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


# ==============================================================================
# BÀI 1: IN BẢNG CỬU CHƯƠNG TỪ A ĐẾN B (HOẶC TỪ B ĐẾN A)
# ==============================================================================
def print_multiplication_tables(a, b):
    # Xác định giá trị bắt đầu (start) và kết thúc (end) dựa trên điều kiện số nào lớn hơn
    start = min(a, b)
    end = max(a, b)
    
    print(f"\n--- BẢNG CỬU CHƯƠNG TỪ {start} ĐẾN {end} ---")
    # Vòng lặp duyệt qua từng bảng cửu chương
    for i in range(start, end + 1):
        print(f"\n[Bảng cửu chương {i}]")
        # Vòng lặp nhân từ 1 đến 10
        for j in range(1, 11):
            # Định dạng căn lề trái {:2d} để kết quả thẳng hàng, đẹp mắt
            print(f"{i} x {j:2d} = {i * j:2d}")


# ==============================================================================
# BÀI 2: KIỂM TRA SỐ NGUYÊN TỐ N
# ==============================================================================
def check_and_print_prime(n):
    if is_prime(n):
        print(f"Số {n} LÀ số nguyên tố.")
    else:
        print(f"Số {n} KHÔNG PHẢI là số nguyên tố.")


# ==============================================================================
# BÀI 3 & 4: LIỆT KÊ VÀ ĐẾM CÁC SỐ NGUYÊN TỐ NHO HƠN N
# Tích hợp cả 2 yêu cầu vào 1 hàm tối ưu để giảm số lần lặp dữ liệu
# ==============================================================================
def list_and_count_primes_less_than_n(n):
    # Sử dụng kỹ thuật List Comprehension để lọc nhanh các số nguyên tố < n
    prime_list = [i for i in range(2, n) if is_prime(i)]
    
    # Bài 3: Liệt kê
    print(f"Các số nguyên tố nhỏ hơn {n} là: ", end="")
    for p in prime_list:
        print(p, end=" ")
        
    # Bài 4: Đếm số lượng phần tử trong danh sách thu được
    print(f"\nSố lượng số nguyên tố nhỏ hơn {n} là: {len(prime_list)}")


# ==============================================================================
# BÀI 5: LIỆT KÊ CÁC ƯỚC SỐ CỦA N LÀ SỐ NGUYÊN TỐ
# ==============================================================================
def list_prime_factors(n):
    prime_factors = []
    
    # Chạy vòng lặp tìm ước số thực sự của n đến căn bậc hai của n (Tối ưu O(sqrt(n)))
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # Nếu i là ước, kiểm tra xem i có phải số nguyên tố không
            if is_prime(i):
                prime_factors.append(i)
            # Kiểm tra ước đối xứng của i là (n // i), loại trừ trường hợp i * i = n
            if i != n // i and is_prime(n // i):
                prime_factors.append(n // i)
                
    # Sắp xếp lại danh sách các ước số nguyên tố theo thứ tự tăng dần
    prime_factors.sort()
    
    print(f"Các số vừa là ước của {n}, vừa là số nguyên tố: ", end="")
    for p in prime_factors:
        print(p, end=" ")
    print()


# ==============================================================================
# HÀM ĐIỀU KHIỂN CHÍNH (MAIN FUNCTION)
# ==============================================================================
def main():
    # --- DEMO BÀI 1 ---
    print("--- BÀI 1 ---")
    try:
        # Sử dụng hàm split(',') để tách chuỗi nhập vào bởi dấu phẩy
        user_input = input("Nhập 2 số nguyên a, b (cách nhau bởi dấu phẩy): ")
        a, b = map(int, user_input.split(','))
        print_multiplication_tables(a, b)
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số nguyên cách nhau bởi dấu phẩy (Ví dụ: 3, 7)")
        
    print("\n" + "="*50 + "\n")

    # --- CHUẨN BỊ DỮ LIỆU CHO BÀI 2, 3, 4, 5 ---
    try:
        n = int(input("Nhập một số nguyên dương n cho các bài tập tiếp theo: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên lớn hơn 0!")
            return
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào phải là số nguyên!")
        return

    # --- DEMO BÀI 2 ---
    print("\n--- BÀI 2 ---")
    check_and_print_prime(n)

    # --- DEMO BÀI 3 & 4 ---
    print("\n--- BÀI 3 & 4 ---")
    list_and_count_primes_less_than_n(n)

    # --- DEMO BÀI 5 ---
    print("\n--- BÀI 5 ---")
    list_prime_factors(n)

if __name__ == "__main__":
    main()
