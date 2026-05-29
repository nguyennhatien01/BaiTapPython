# 1. nhập dữ liệu 
# Nhập các kích thước hình khối (kiểu số thực)
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
# Nhập số chữ số thập phân muốn hiển thị (kiểu số nguyên)
so_le = int(input("Số lượng số lẻ cần hiển thị: "))
# Khai báo mã UNICODE cho ký tự số mũ 2 và 3
mu_2 = "\u00b2"  
mu_3 = "\u00b3"  

# 2. tính toán
dien_tich_day = dai * rong
the_tich = dien_tich_day * cao

# 3. in kết quả
print("\n--- KẾT QUẢ ĐÃ XỬ LÝ (CÁCH 1) ---")
# Sử dụng F-string 
print(f"Cách 1: Diện tích đáy hình chữ nhật = {dien_tich_day:.{so_le}f}cm{mu_2}")
print(f"Cách 1: Thể tích hình khối = {the_tich:.{so_le}f}cm{mu_3}")
