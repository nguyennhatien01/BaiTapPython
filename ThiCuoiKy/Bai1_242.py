# Nhập các kích thước hình khối (kiểu số thực)
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
# Nhập số chữ số thập phân muốn hiển thị (kiểu số nguyên)
sole = int(input("Số lượng số lẻ cần hiển thị: "))
# Khai báo mã UNICODE cho ký tự số mũ 2 và 3
mu2 = "\u00b2"  
mu3 = "\u00b3"  

# 2. tính toán
dientichday = dai * rong
thetich = dientichday * cao

# 3. in kết quả
print(f"Diện tích đáy hình chữ nhật = {dientichday:.{sole}f}cm{mu2}")
print(f"Thể tích hình khối = {thetich:.{sole}f}cm{mu3}")
