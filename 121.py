def find_strobogrammatic(n, is_extended=False):
    """
    Hàm phát sinh danh sách các chuỗi strobogrammatic có độ dài n.
    is_extended = False: Chuẩn cơ bản (0, 1, 6, 8, 9)
    is_extended = True: Chuẩn mở rộng (bổ sung 2, 5)
    """
    # Các cặp chữ số đối xứng qua phép xoay 180 độ
    if not is_extended:
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        single_digits = ['0', '1', '8']
    else:
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6'), ('2', '2'), ('5', '5')]
        single_digits = ['0', '1', '8', '2', '5']

    def helper(m):
        # Trường hợp cơ sở cho đệ quy
        if m == 0:
            return [""]
        if m == 1:
            return single_digits
        
        # Đệ quy cho bài toán con nhỏ hơn 2 chữ số
        sub_list = helper(m - 2)
        res = []
        
        for s in sub_list:
            for p in pairs:
                # Không được thêm số '0' ở đầu nếu đây là tầng ngoài cùng (độ dài đầy đủ n)
                if p[0] == '0' and m == n:
                    continue
                res.append(p[0] + s + p[1])
        return res

    return helper(n)

# --- CHƯƠNG TRÌNH CHÍNH ---
try:
    n = int(input("Nhập số nguyên n (2 <= n <= 10): "))
    if 2 <= n <= 10:
        # Câu a: Strobogrammatic cơ bản
        result_a = find_strobogrammatic(n, is_extended=False)
        print(f"\na.- Tất cả các số strobogrammatic gồm {n} chữ số (Tổng cộng: {len(result_a)} số):")
        # In tối đa 50 số đầu tiên để tránh tràn màn hình khi n lớn
        print(", ".join(result_a[:50]) + ("..." if len(result_a) > 50 else ""))
        
        # Câu b: Strobogrammatic mở rộng
        result_b = find_strobogrammatic(n, is_extended=True)
        print(f"\nb.- Tất cả các số strobogrammatic mở rộng gồm {n} chữ số (Tổng cộng: {len(result_b)} số):")
        print(", ".join(result_b[:50]) + ("..." if len(result_b) > 50 else ""))
    else:
        print("Vui lòng nhập n trong khoảng từ 2 đến 10.")
except ValueError:
    print("Dữ liệu nhập vào phải là một số nguyên.")
