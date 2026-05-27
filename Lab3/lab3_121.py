# ==============================================================================
# HÀM ĐỆ QUY TỔNG QUÁT ĐỂ SINH SỐ STROBOGRAMMATIC
# n: độ dài hiện tại cần sinh
# max_n: độ dài ban đầu được nhập từ bàn phím (để chặn không cho số 0 đứng đầu)
# pairs: tập hợp các cặp đối xứng tương ứng (chuẩn hoặc mở rộng)
# ==============================================================================
def find_strobogrammatic_helper(n, max_n, pairs):
    # Trường hợp cơ sở 1: Độ dài bằng 0, trả về một chuỗi rỗng
    if n == 0:
        return [""]
    # Trường hợp cơ sở 2: Độ dài bằng 1, trả về các chữ số tự đối xứng đơn lẻ
    if n == 1:
        # Lọc ra các số tự đối xứng (chỉ số có cặp dạng 'x' đi với 'x')
        return [l for l, r in pairs if l == r]

    # Gọi đệ quy quy nạp: Lấy danh sách các chuỗi có độ dài (n - 2)
    sub_list = find_strobogrammatic_helper(n - 2, max_n, pairs)
    result = []

    # Duyệt qua từng chuỗi con đã sinh được ở bước trước
    for s in sub_list:
        # Duyệt qua từng cặp số đối xứng xoay 180 độ
        for l, r in pairs:
            # Điều kiện chặn: Không cho phép chữ số '0' đứng ở vị trí đầu tiên của số gốc
            if l == '0' and n == max_n:
                continue
            # Ghép cặp ký tự vào hai đầu của chuỗi con
            result.append(l + s + r)

    return result

# ==============================================================================
# CÂU A: Sinh số Strobogrammatic chuẩn
# ==============================================================================
def generate_strobogrammatic(n):
    # Tập các cặp ký tự đối xứng chuẩn khi xoay 180 độ
    standard_pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
    return find_strobogrammatic_helper(n, n, standard_pairs)

# ==============================================================================
# CÂU B: Sinh số Strobogrammatic mở rộng
# ==============================================================================
def generate_strobogrammatic_extended(n):
    # Tập các cặp ký tự mở rộng (bổ sung thêm cặp tự đối xứng 2-2 và 5-5)
    extended_pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6'), ('2', '2'), ('5', '5')]
    return find_strobogrammatic_helper(n, n, extended_pairs)

# ==============================================================================
# HÀM MAIN - ĐIỀU KHIỂN CHƯƠNG TRÌNH CHÍNH
# ==============================================================================
def main():
    # Nhập dữ liệu từ bàn phím và ép kiểu sang số nguyên
    try:
        n = int(input("Nhap so nguyen n (2 <= n <= 10): "))
        if not (2 <= n <= 10):
            print("Gia tri n phai nam trong doan [2, 10]!")
            return
    except ValueError:
        print("Vui long nhap mot so nguyen hop le!")
        return

    # --- THỰC HIỆN CÂU A ---
    print(f"\na.- Tat ca cac so strobogrammatic gom {n} chu so:")
    result_a = generate_strobogrammatic(n)
    # Sắp xếp lại danh sách theo thứ tự tăng dần trước khi in ra
    result_a.sort(key=int)
    for num in result_a:
        print(num, end=" ")
    print(f"\n=> Tong cong co: {len(result_a)} so.")
    print("\n" + "="*60)

    # --- THỰC HIỆN CÂU B ---
    print(f"\nb.- Tat ca cac so strobogrammatic mo rong gom {n} chu so:")
    result_b = generate_strobogrammatic_extended(n)
    # Sắp xếp lại danh sách theo thứ tự tăng dần trước khi in ra
    result_b.sort(key=int)
    for num in result_b:
        print(num, end=" ")
    print(f"\n=> Tong cong co: {len(result_b)} so.")

if __name__ == "__main__":
    main()
