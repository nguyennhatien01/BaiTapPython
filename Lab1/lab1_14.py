# ==============================================================================
# BÀI 14: BÀI TOÁN ĐỔI TIỀN THEO THUẬT TOÁN THAM LAM (GREEDY ALGORITHM)
# Kỹ thuật áp dụng: Sử dụng List lưu mệnh giá, vòng lặp for, phép toán // và %
# ==============================================================================

def main():
    # Nhập số tiền X từ bàn phím và ép kiểu về số nguyên int
    try:
        X = int(input("Nhập số tiền X cần đổi: "))
        if X < 0:
            print("Số tiền nhập vào không được âm!")
            return
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
        return

    # Lưu trữ số tiền gốc ban đầu để in ra kết quả ở phần sau
    so_tien_goc = X

    # Danh sách (List) chứa 9 loại mệnh giá tiền, sắp xếp từ lớn đến nhỏ để ưu tiên đổi trước
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    # Biến tích lũy dùng để đếm tổng số tờ tiền của tất cả các loại sau khi đổi
    tong_so_to = 0

    print(f"\nSo tien {so_tien_goc} duoc doi thanh:")

    # Vòng lặp duyệt qua từng mệnh giá tiền trong danh sách từ lớn đến nhỏ
    for value in menh_gia:
        # Tính số tờ tiền có thể đổi được của mệnh giá hiện tại (Dùng phép chia lấy nguyên //)
        so_to = X // value
        
        # Cập nhật lại số tiền còn dư sau khi đã đổi mệnh giá hiện tại (Dùng phép chia lấy dư %)
        X = X % value
        
        # Cộng dồn số tờ tiền vừa đổi được vào biến tổng
        tong_so_to += so_to
        
        # In ra số lượng tờ tiền của mệnh giá hiện tại theo đúng định dạng mẫu của đề bài
        print(f"Loai {value} gom {so_to} to")

    # In ra tổng cộng số tờ tiền thu được sau khi kết thúc vòng lặp
    print(f"TỔNG CỘNG CÓ {tong_so_to} TỜ")

if __name__ == "__main__":
    main()
