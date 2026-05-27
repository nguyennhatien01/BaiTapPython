# ==============================================================================
# BÀI 20: BÀI TOÁN ĐỔI TIỀN NÂNG CẤP VÀ ỨNG DỤNG QUẢN LÝ THU NGÂN
# Kỹ thuật áp dụng: Hàm chia nhỏ module, Tham lam (Greedy), cấu trúc rẽ nhánh rành mạch
# ==============================================================================

def tinh_va_in_tien_thoi(so_tien_thoi):
    """
    Hàm nhận vào số tiền cần thối lại, thực hiện phân tích thành các mệnh giá
    sao cho số tờ là ít nhất và CHỈ IN những loại tiền có số tờ lớn hơn 0.
    """
    # Danh sách 9 loại mệnh giá tiền từ lớn đến nhỏ
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    tong_so_to = 0  # Biến đếm tổng số lượng tờ tiền thối lại
    tong_so_loai = 0  # Biến đếm số lượng loại tiền thực tế được sử dụng (số tờ > 0)

    print(f"\nSo tien {so_tien_thoi} duoc doi thanh:")

    # Duyệt qua từng mệnh giá để tính toán
    for value in menh_gia:
        so_to = so_tien_thoi // value  # Chia lấy phần nguyên để được số tờ
        so_tien_thoi = so_tien_thoi % value  # Chia lấy dư để cập nhật số tiền còn lại

        # ĐIỀU KIỆN CHỈ IN: Chỉ xử lý và in khi số lượng tờ lớn hơn 0
        if so_to > 0:
            print(f"Loai {value} gom {so_to} to")
            tong_so_to += so_to  # Cộng dồn số tờ
            tong_so_loai += 1  # Tăng số loại tiền đã dùng lên 1

    # In các dòng tổng kết theo yêu cầu mẫu mới của đề bài
    print(f"TỔNG CỘNG CÓ {tong_so_to} TỜ")
    print(f"Tong so loai = {tong_so_loai}")


def main():
    print("=== CHƯƠNG TRÌNH QUẢN LÝ QUẦY THU NGÂN ===")
    
    # --- PHẦN MỞ RỘNG: NHẬP DỮ LIỆU ĐẦU VÀO ---
    try:
        a = int(input("Nhập số tiền hàng cần trả (a): "))
        b = int(input("Nhập số tiền khách hàng thực tế trả (b): "))
        if a < 0 or b < 0:
            print("Số tiền nhập vào không được phép âm!")
            return
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
        return

    # --- BIỆN LUẬN CÁC TRƯỜNG HỢP THEO YÊU CẦU ĐỀ BÀI ---
    
    # Trường hợp 1: Khách trả thiếu tiền (b < a)
    if b < a:
        tien_thieu = a - b
        print(f"Thông báo: Số tiền khách hàng còn thiếu là {tien_thieu}.")
        # Chương trình kết thúc tại đây theo yêu cầu
        
    # Trường hợp 2: Khách trả vừa đủ tiền (b == a)
    elif b == a:
        print("Cám ơn khách hàng. Hẹn gặp lại")
        # Chương trình kết thúc tại đây theo yêu cầu
        
    # Trường hợp 3: Khách trả dư tiền (b > a) -> Cần thối lại tiền
    else:
        tien_thoi_lai = b - a
        print(f"Khách trả dư. Số tiền cần thối lại cho khách là: {tien_thoi_lai}")
        
        # Gọi lại module xử lý thuật toán đổi tiền đã viết ở trên
        tinh_va_in_tien_thoi(tien_thoi_lai)
        
        # Đợi người dùng nhấn phím Enter để xác nhận hoàn tất giao dịch
        print("\n--------------------------------------------------")
        input("Nhấn phím ENTER để hoàn tất quá trình thối tiền...")
        
        # Xuất câu chào kết thúc giao dịch
        print("Cám ơn khách hàng. Hẹn gặp lại")

if __name__ == "__main__":
    main()
