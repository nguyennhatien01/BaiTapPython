import math

MAX_LIMIT = 1000000  # Giới hạn đề bài yêu cầu (1 triệu)

# ==============================================================================
# HÀM SÀNG SỐ NGUYÊN TỐ ERATOSTHENES
# Tối ưu hóa việc kiểm tra số nguyên tố chỉ mất O(1) sau khi sàng xong
# ==============================================================================
is_prime = [True] * MAX_LIMIT  # Khởi tạo mảng đánh dấu, mặc định coi tất cả là số nguyên tố
is_prime[0] = is_prime[1] = False  # 0 và 1 không phải là số nguyên tố

def sieve():
    # Vòng lặp chạy từ 2 đến căn bậc hai của MAX_LIMIT
    for i in range(2, int(math.sqrt(MAX_LIMIT)) + 1):
        if is_prime[i]:
            # Nếu i là số nguyên tố, ta đánh dấu tất cả các bội của i là False
            for j in range(i * i, MAX_LIMIT, i):
                is_prime[j] = False

# ==============================================================================
# KỸ THUẬT HAI CON TRỎ KIỂM TRA ĐỐI XỨNG XOAY 180 ĐỘ
# ==============================================================================

# Câu a, b: Kiểm tra số Strobogrammatic chuẩn
def is_strobogrammatic(n):
    s = str(n)  # Chuyển số sang chuỗi để dễ duyệt từng ký tự
    left = 0
    right = len(s) - 1
    
    # Sử dụng 2 con trỏ chạy từ 2 đầu tiến vào giữa
    while left <= right:
        l = s[left]
        r = s[right]
        
        # Kiểm tra xem cặp ký tự hai đầu có đối xứng hợp lệ khi xoay 180 độ không
        if l == '0' and r == '0': left += 1; right -= 1
        elif l == '1' and r == '1': left += 1; right -= 1
        elif l == '8' and r == '8': left += 1; right -= 1
        elif l == '6' and r == '9': left += 1; right -= 1
        elif l == '9' and r == '6': left += 1; right -= 1
        else:
            return False  # Gặp cặp ký tự không hợp lệ thì trả về False ngay lập tức
    return True

# Câu c, d: Kiểm tra số Strobogrammatic mở rộng (bổ sung thêm số 2 và 5 theo đề)
def is_strobogrammatic_extended(n):
    s = str(n)
    left = 0
    right = len(s) - 1
    
    while left <= right:
        l = s[left]
        r = s[right]
        
        if l == '0' and r == '0': left += 1; right -= 1
        elif l == '1' and r == '1': left += 1; right -= 1
        elif l == '8' and r == '8': left += 1; right -= 1
        elif l == '6' and r == '9': left += 1; right -= 1
        elif l == '9' and r == '6': left += 1; right -= 1
        elif l == '2' and r == '2': left += 1; right -= 1  # Thêm số 2 tự đối xứng
        elif l == '5' and r == '5': left += 1; right -= 1  # Thêm số 5 tự đối xứng
        else:
            return False
    return True

# Câu e: Hàm thực hiện xoay một số 180 độ
def rotate_180(n):
    s = str(n)
    rotated_str = ""
    
    # Duyệt ngược từ cuối chuỗi lên đầu chuỗi (vì xoay 180 độ thì ký tự cuối sẽ lên đầu)
    for char in reversed(s):
        if char == '0': rotated_str += '0'
        elif char == '1': rotated_str += '1'
        elif char == '2': rotated_str += '2'
        elif char == '5': rotated_str += '5'
        elif char == '8': rotated_str += '8'
        elif char == '6': rotated_str += '9'  # Số 6 xoay ngược thành số 9
        elif char == '9': rotated_str += '6'  # Số 9 xoay ngược thành số 6
        else:
            return -1  # Trả về -1 nếu chứa ký tự không thể xoay (như 3, 4, 7)
            
    return int(rotated_str)  # Chuyển chuỗi kết quả sau khi xoay về lại kiểu số nguyên

# ==============================================================================
# HÀM MAIN - ĐIỀU KHIỂN CHƯƠNG TRÌNH CHÍNH
# ==============================================================================
def main():
    sieve()  # Gọi hàm sàng để chuẩn bị sẵn mảng kiểm tra số nguyên tố nhanh

    # --- CÂU A ---
    print("a.- Cac so strobogrammatic nho hon 1 trieu:")
    for i in range(1, MAX_LIMIT):
        if is_strobogrammatic(i):
            print(i, end=" ")
    print("\n\n" + "-"*50 + "\n")

    # --- CÂU B ---
    print("b.- Cac so nguyen to strobogrammatic nho hon 1 trieu:")
    for i in range(1, MAX_LIMIT):
        if is_prime[i] and is_strobogrammatic(i):
            print(i, end=" ")
    print("\n\n" + "-"*50 + "\n")

    # --- CÂU C ---
    print("c.- Cac so strobogrammatic mo rong nho hon 1 trieu:")
    for i in range(1, MAX_LIMIT):
        if is_strobogrammatic_extended(i):
            print(i, end=" ")
    print("\n\n" + "-"*50 + "\n")

    # --- CÂU D ---
    print("d.- Cac so nguyen to strobogrammatic mo rong nho hon 1 trieu:")
    for i in range(1, MAX_LIMIT):
        if is_prime[i] and is_strobogrammatic_extended(i):
            print(i, end=" ")
    print("\n\n" + "-"*50 + "\n")

    # --- CÂU E ---
    print("e.- Cac so thoa man dieu kien cau e:")
    for i in range(1, MAX_LIMIT):
        # Điều kiện 1: Không phải số nguyên tố VÀ không phải là số strobogrammatic mở rộng
        if not is_prime[i] and not is_strobogrammatic_extended(i):
            rotated_value = rotate_180(i)  # Tiến hành xoay số này 180 độ
            
            # Điều kiện 2: Số xoay phải hợp lệ (!= -1) và giá trị sau khi xoay PHẢI là số nguyên tố
            if rotated_value != -1 and is_prime[rotated_value]:
                print(f"{i} (Xoay thanh: {rotated_value})")

if __name__ == "__main__":
    main()
