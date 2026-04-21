from datetime import datetime, timedelta

# i
print("=== CÂU i ===")
now = datetime.now()
print("Năm hiện tại:", now.year)
print("Tháng hiện tại bằng chữ:", now.strftime("%B"))
print("Tuần trong năm:", now.strftime("%U"))
print("Tuần trong tháng:", (now.day - 1)//7 + 1)
print("Ngày trong năm:", now.strftime("%j"))
print("Ngày dương lịch:", now.day)
print("Thứ:", now.strftime("%A"))
print("Giờ hiện tại:", now.strftime("%H:%M:%S"))

# ii
print("\n=== CÂU ii ===")
d1 = input("Nhập ngày thứ nhất (dd/mm/yyyy): ")
d2 = input("Nhập ngày thứ hai (dd/mm/yyyy): ")

date1 = datetime.strptime(d1, "%d/%m/%Y")
date2 = datetime.strptime(d2, "%d/%m/%Y")

print("Số ngày cách nhau:", abs((date2 - date1).days))

# iii
print("\n=== CÂU iii ===")
S = input("Nhập chuỗi ngày (vd: Sep 18 2019 2:43PM): ")
date_obj = datetime.strptime(S, "%b %d %Y %I:%M%p")
print("Sau khi chuyển:", date_obj)

# iv
print("\n=== CÂU iv ===")
print("Sau khi thêm 5 giây:", (datetime.now() + timedelta(seconds=5)))