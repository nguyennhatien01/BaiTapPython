import math

def is_friendly_number(n):
    """
    Hàm kiểm tra một số có phải là số thân thiện hay không.
    Trả về True nếu ước chung lớn nhất của số đó và số đảo ngược của nó bằng 1.
    """
    # Bước 1: Đảo ngược số bằng kỹ thuật cắt chuỗi [::-1]
    reversed_str = str(n)[::-1]
    reversed_num = int(reversed_str)
    
    # Bước 2: Kiểm tra xem GCD của hai số có bằng 1 không
    return math.gcd(n, reversed_num) == 1

def main_114():
    print("=== BÀI 114: TÌM SỐ THÂN THIỆN ===")
    
    # Nhập hai số nguyên a và b từ bàn phím trên cùng một dòng
    try:
        user_input = input("Nhập hai số a và b (cách nhau bởi dấu cách): ")
        a, b = map(int, user_input.split())
        
        # Kiểm tra điều kiện ràng buộc của đề bài
        if not (10 <= a <= b <= 30000):
            print("Lỗi: Vui lòng nhập đúng điều kiện 10 <= a <= b <= 30000")
            return
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào phải là số nguyên!")
        return

    # Khởi tạo danh sách chứa các số thân thiện tìm được
    friendly_list = []
    
    # Vòng lặp duyệt qua tất cả các số từ a đến b (kể cả b)
    for i in range(a, b + 1):
        if is_friendly_number(i):
            friendly_list.append(i)
            
    # --- XUẤT KẾT QUẢ ---
    print(f"\nCác số thân thiện trong khoảng từ {a} đến {b} là:")
    for num in friendly_list:
        print(num, end=" ")
        
    print(f"\n\n=> Tổng số lượng số thân thiện tìm được là: {len(friendly_list)} số.")

if __name__ == "__main__":
    main_114()
