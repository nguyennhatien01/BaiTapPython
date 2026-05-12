# Danh sách các mệnh giá tiền
money = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền
x = int(input("Nhập số tiền X: "))

# Lưu số tiền ban đầu
so_tien_goc = x

# Tổng số tờ tiền
tong_to = 0

# Tổng số loại tiền được dùng
tong_loai = 0

# In tiêu đề
print("\nSố tiền", so_tien_goc, "được đổi thành:")

# Duyệt từng loại tiền
for value in money:

    # Tính số tờ
    so_to = x // value

    # Cập nhật số tiền còn lại
    x = x % value

    # Chỉ in nếu số tờ > 0
    if so_to > 0:

        print("Loại", value, "gồm", so_to, "tờ")

        # Cộng tổng số tờ
        tong_to += so_to

        # Cộng số loại tiền
        tong_loai += 1

# In tổng kết
print("\nTỔNG CỘNG CÓ", tong_to, "TỜ")
print("Tổng số loại tiền =", tong_loai)