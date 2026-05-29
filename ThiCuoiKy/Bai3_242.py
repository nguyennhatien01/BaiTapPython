# kiểm tra xem có phải là bội số của 13 hoặc 19 hay không
# trả về True nếu n là bội của 13 hoặc 19, ngược lại trả về False
kiemtraboiso = lambda n: n % 13 == 0 or n % 19 == 0


# kiểm tra xem a b c có phải là 3 cạnh của tam giác hay không
istamgiac = lambda a, b, c: a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

# Dùng toán tử ba ngôi (Ternary Operator) lồng nhau để viết trên 1 dòng lambda
loaitamgiac = lambda a, b, c: (
    "Đều" if a == b == c else
    "Cân" if (a == b or b == c or a == c) and not (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) else
    "Vuông Cân" if (a == b or b == c or a == c) and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) else
    "Vuông" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else
    "Thường"
)

# chạy trương chình và in kết quả 
print("---Kiểm tra bội số---")
n = int(input("Nhập số nguyên n: "))
kqboiso = "CÓ" if kiemtraboiso(n) else "KHÔNG"
print(f"Số {n} {kqboiso} là bội số của 13 hoặc 19")


print("\n---Kiểm tra tam giác---")
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if istamgiac(a, b, c):
    loaitamgiac = loaitamgiac(a, b, c)
    print(f"Kết quả phân loại: {loaitamgiac}")
else:
    print("Ba cạnh không tạo thành tam giác.")