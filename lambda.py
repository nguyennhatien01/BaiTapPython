import math

# a) Trị tuyệt đối
tri_tuyet_doi = lambda n: abs(n)

# b) n + 15
cong_15 = lambda n: n + 15

# c) Tích x và y
tich = lambda x, y: x * y

# d) Kiểm tra bội số của 13 hoặc 19
boi_so = lambda n: (n % 13 == 0) or (n % 19 == 0)

# e) Diện tích hình tròn
dien_tich_tron = lambda r: math.pi * r * r

# f) Chu vi hình chữ nhật
chu_vi_hcn = lambda d, r: 2 * (d + r)

# g) Kiểm tra số chính phương
so_chinh_phuong = lambda n: int(math.sqrt(n))**2 == n

# h) Kiểm tra số nguyên tố
so_nguyen_to = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# i) Kiểm tra và phân loại tam giác
tam_giac = lambda a, b, c: (
    "Không phải tam giác"
    if a + b <= c or a + c <= b or b + c <= a
    else "Tam giác đều"
    if a == b == c
    else "Tam giác vuông"
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
    else "Tam giác cân"
    if a == b or b == c or a == c
    else "Tam giác thường"
)

# =========================
# Chương trình chính
# =========================

n = int(input("Nhập số nguyên n: "))

print("a) Trị tuyệt đối của n:", tri_tuyet_doi(n))
print("b) n + 15 =", cong_15(n))
print("d) n có là bội của 13 hoặc 19 không:", boi_so(n))
print("g) n có phải số chính phương không:", so_chinh_phuong(n))
print("h) n có phải số nguyên tố không:", so_nguyen_to(n))

x = int(input("\nNhập x: "))
y = int(input("Nhập y: "))
print("c) Tích x * y =", tich(x, y))

r = float(input("\nNhập bán kính hình tròn: "))
print("e) Diện tích hình tròn =", dien_tich_tron(r))

d = float(input("\nNhập chiều dài hình chữ nhật: "))
rong = float(input("Nhập chiều rộng hình chữ nhật: "))
print("f) Chu vi hình chữ nhật =", chu_vi_hcn(d, rong))

a = int(input("\nNhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
print("i) Loại tam giác:", tam_giac(a, b, c))