def solve_subnumber_squares(n):
    """
    Hàm sinh ra tất cả các số con từ số n, tính bình phương và cộng dồn vào tổng S.
    """
    s = str(n)  # Chuyển số n thành chuỗi để thực hiện cắt chuỗi con
    length = len(s)
    total_sum = 0  # Biến tích lũy tổng bình phương S

    print(f"\nCác số con tách ra từ {n} là:")
    
    # Vòng lặp i quản lý vị trí bắt đầu của chuỗi con
    for i in range(length):
        # Vòng lặp j quản lý vị trí kết thúc (cộng thêm 1 để lấy trọn ký tự cuối)
        for j in range(i + 1, length + 1):
            sub_str = s[i:j]  # Cắt chuỗi con bằng kỹ thuật slicing
            sub_num = int(sub_str)  # Ép kiểu chuỗi con vừa cắt thành số nguyên
            
            print(sub_num, end="  ")  # In ra màn hình để theo dõi trực quan
            total_sum += sub_num ** 2  # Tính bình phương rồi cộng dồn vào tổng

    return total_sum

def main_117():
    print("\n" + "="*50 + "\n")
    print("=== BÀI 117: TỔNG BÌNH PHƯƠNG SỐ CON ===")
    
    # Nhập số nguyên dương n từ bàn phím
    try:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n <= 0:
            print("Lỗi: Số nhập vào phải lớn hơn 0!")
            return
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
        return

    # Gọi hàm xử lý thuật toán
    S = solve_subnumber_squares(n)
    
    # Xuất tổng kết quả cuối cùng
    print(f"\n\n=> Tổng bình phương các số con S = {S}")

if __name__ == "__main__":
    main_117()
