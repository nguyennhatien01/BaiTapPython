import math

# ==============================================================================
# XÂY DỰNG CÁC HÀM ẨN DANH (LAMBDA FUNCTIONS) TỪ 1 ĐẾN 9
# ==============================================================================

# 1) Hàm trả về trị tuyệt đối của n (Sử dụng hàm abs có sẵn)
get_absolute_value = lambda n: abs(n)

# 2) Hàm trả về giá trị của n + 15
add_fifteen = lambda n: n + 15

# 3) Hàm nhận 2 đối số (x, y) và trả về tích của x và y
get_product = lambda x, y: x * y

# 4) Hàm kiểm tra n có phải là bội số của 13 hoặc 19 hay không
# Sử dụng toán tử toán học chia lấy dư %
is_multiple_13_or_19 = lambda n: n % 13 == 0 or n % 19 == 0

# 5) Hàm nhận bán kính r và trả về diện tích hình tròn (Sử dụng hằng số math.pi)
get_circle_area = lambda r: math.pi * (r ** 2)

# 6) Hàm nhận chiều dài d, chiều rộng r và trả về chu vi hình chữ nhật
get_rectangle_perimeter = lambda d, r: (d + r) * 2

# 7) Hàm kiểm tra n có phải là số chính phương hay không
# Sử dụng math.isqrt(n) để lấy phần nguyên căn bậc hai, tránh sai số số thực float
is_perfect_square = lambda n: n >= 0 and math.isqrt(n) ** 2 == n

# 8) Hàm kiểm tra n có phải là số nguyên tố hay không
# Sử dụng hàm all() để kiểm tra n không chia hết cho bất kỳ số nào từ 2 đến căn bậc hai của n
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, math.isqrt(n) + 1))

# 9) Hàm nhận 3 cạnh (a, b, c): Kiểm tra xem có lập thành tam giác không, nếu có thì là tam giác gì?
# Sử dụng cấu trúc rẽ nhánh inline (Ternary Operator) lồng nhau để phân loại tam giác
classify_triangle = lambda a, b, c: (
    "Không phải tam giác" if not (a + b > c and a + c > b and b + c > a) else
    "Tam giác đều" if a == b == c else
    "Tam giác vuông cân" if (a==b or b==c or a==c) and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác vuông" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else
    "Tam giác thường"
)

# ==============================================================================
# HÀM MAIN - CHẠY THỬ NGHIỆM VÀ KIỂM TRA KẾT QUẢ TỪNG CÂU
# ==============================================================================
def main():
    print("--- KẾT QUẢ CHẠY THỬ NGHIỆM CÁC HÀM LAMBDA ---")
    
    print(f"1) Trị tuyệt đối của -10: {get_absolute_value(-10)}")
    print(f"2) Giá trị của 5 + 15: {add_fifteen(5)}")
    print(f"3) Tích của 4 và 7: {get_product(4, 7)}")
    print(f"4) Số 26 có phải bội của 13 hoặc 19? {is_multiple_13_or_19(26)}")
    print(f"5) Diện tích hình tròn có bán kính r = 3.5: {get_circle_area(3.5):.2f}")
    print(f"6) Chu vi hình chữ nhật d = 5.5, r = 2.5: {get_rectangle_perimeter(5.5, 2.5)}")
    print(f"7) Số 16 có phải số chính phương? {is_perfect_square(16)}")
    print(f"8) Số 17 có phải số nguyên tố? {is_prime(17)}")
    
    print("\n9) Kiểm tra phân loại tam giác:")
    print(f"   - Ba cạnh 3, 4, 5 là: {classify_triangle(3, 4, 5)}")
    print(f"   - Ba cạnh 5, 5, 5 là: {classify_triangle(5, 5, 5)}")
    print(f"   - Ba cạnh 4, 4, 6 là: {classify_triangle(4, 4, 6)}")
    print(f"   - Ba cạnh 1, 2, 8 là: {classify_triangle(1, 2, 8)}")

if __name__ == "__main__":
    main()
