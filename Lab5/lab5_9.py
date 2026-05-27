# ==============================================================================
# BÀI 9: TÍNH DIỆN TÍCH VÀ THỂ TÍCH HÌNH KHỐI CHỮ NHẬT
# Kỹ thuật áp dụng: Ép kiểu số thực, định dạng chuỗi động (Dynamic String Formatting)
# ==============================================================================

def main():
    # --- BƯỚC 1: NHẬP DỮ LIỆU ĐẦU VÀO VÀ ÉP KIỂU ---
    # Nhập các kích thước hình khối (kiểu số thực float)
    chieu_dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm):>? "))
    chieu_rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm):>? "))
    chieu_cao = float(input("Nhập chiều cao hình khối chữ nhật (cm):>? "))
    
    # Nhập số lượng số lẻ cần hiển thị (kiểu số nguyên int)
    so_le = int(input("Số lượng số lẻ cần hiển thị:> "))

    # --- BƯỚC 2: TÍNH TOÁN CÁC ĐẠI LƯỢNG ---
    # Diện tích đáy hình chữ nhật = dài * rộng
    dien_tich_day = chieu_dai * chieu_rong
    
    # Thể tích hình khối chữ nhật = diện tích đáy * chiều cao
    the_tich = dien_tich_day * chieu_cao

    # --- BƯỚC 3: ĐỊNH DẠNG KÝ TỰ MŨ UNICODE ---
    # Mã Unicode cho số mũ 2 (²) và số mũ 3 (³) theo gợi ý của đề bài
    mu_2 = "\u00b2"
    mu_3 = "\u00b3"

    # --- BƯỚC 4: XUẤT KẾT QUẢ THEO 2 CÁCH ĐỊNH DẠNG ---
    print("\n--- KẾT QUẢ ---")

    # --- XỬ LÝ DIỆN TÍCH ĐÁY ---
    # Cách 1: Sử dụng hàm format() truyền thống của Python
    # Cú pháp "{:.{}f}".format(value, precision) giúp truyền động số lượng chữ số lẻ
    print("Cách 1: Diện tích đáy hình chữ nhật = {:.{}f}cm{}".format(dien_tich_day, so_le, mu_2))
    
    # Cách 2: Sử dụng F-string (được ưa chuộng từ Python 3.6+) lồng biểu thức định dạng số lẻ
    print(f"Cách 2: Diện tích đáy hình chữ nhật = {dien_tich_day:.{so_le}f}cm{mu_2}")


    # --- XỬ LÝ THỂ TÍCH ---
    # Cách 1: Sử dụng hàm format() truyền thống
    print("Cách 1: Thể tích hình khối= {:.{}f}cm{}".format(the_tich, so_le, mu_3))
    
    # Cách 2: Sử dụng F-string lồng biểu thức định dạng số lẻ
    print(f"Cách 2: Thể tích hình khối= {the_tich:.{so_le}f}cm{mu_3}")

if __name__ == "__main__":
    main()
