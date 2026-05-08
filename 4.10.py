# ==========================================
# BÀI 1: XỬ LÝ CHUỖI TRONG PYTHON
# ==========================================

# ==========================================
# PHẦN 1:
# TÌM CÁC CHỮ SỐ KHÔNG XUẤT HIỆN
# ==========================================

print("===== PHẦN 1 =====")

# Nhập số điện thoại
sdt = input("Nhập số điện thoại: ")

# Danh sách lưu các số không xuất hiện
khong_xuat_hien = []

# Kiểm tra từ 0 -> 9
for i in range(10):

    # Nếu số không có trong chuỗi
    if str(i) not in sdt:
        khong_xuat_hien.append(i)

# In kết quả
print("Các chữ số không xuất hiện là:")
print(khong_xuat_hien)

# ==========================================
# PHẦN 2:
# TÌM TỪ ĐẦU TIÊN LẶP LẠI
# ==========================================

print("\n===== PHẦN 2 =====")

# Nhập chuỗi
s = input("Nhập chuỗi: ")

# Tách chuỗi thành danh sách từ
words = s.split()

# Danh sách lưu các từ đã xuất hiện
da_xuat_hien = []

# Biến lưu kết quả
ket_qua = None

# Duyệt từng từ
for word in words:

    # Nếu từ đã tồn tại
    if word in da_xuat_hien:
        ket_qua = word
        break

    # Nếu chưa có thì thêm vào danh sách
    da_xuat_hien.append(word)

# In kết quả
print("Từ lặp đầu tiên là:")
print(ket_qua)