# Danh sách các mệnh giá tiền
money = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền cần đổi
x = int(input("Nhập số tiền X: "))

# Lưu lại số tiền ban đầu
so_tien_goc = x

# Biến đếm tổng số tờ tiền
tong_to = 0

# In tiêu đề
print("\nSố tiền", so_tien_goc, "được đổi thành:")

# Duyệt từng loại tiền
for value in money:

    # Tính số tờ tiền của loại hiện tại
    so_to = x // value

    # Tính số tiền còn lại
    x = x % value

    # Cộng vào tổng số tờ
    tong_to += so_to

    # In kết quả
    print("Loại", value, "gồm", so_to, "tờ")

# In tổng số tờ
print("\nTỔNG CỘNG CÓ", tong_to, "TỜ")