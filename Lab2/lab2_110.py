# ==============================================================================
# BÀI 110: GIẢI NÉN CHUỖI KÝ TỰ (CIPHER TEXT -> PLAIN TEXT)
# Kỹ thuật: Vòng lặp while kiểm soát chỉ mục, toán tử nhân chuỗi Python
# ==============================================================================

def giai_nen_chuoi(cipher_text):
    plain_text = ""  # Khởi tạo chuỗi rỗng tích lũy kết quả
    i = 0           # Chỉ mục dùng để duyệt ký tự
    n = len(cipher_text) # Lấy chiều dài của chuỗi nén

    # Vòng lặp while giúp chủ động điều khiển bước nhảy i
    while i < n:
        # Nếu gặp ký tự báo hiệu nén '#'
        if cipher_text[i] == '#':
            # Ký tự i+1 là số lượng lặp (ép kiểu int)
            so_luong = int(cipher_text[i + 1])
            
            # Ký tự i+2 là ký tự gốc cần nhân bản
            ky_tu = cipher_text[i + 2]
            
            # Nhân chuỗi để giải nén tự động trong Python
            plain_text += ky_tu * so_luong
            
            # Nhảy qua 3 ký tự (dấu #, số lượng, ký tự)
            i += 3
        else:
            # Nếu là ký tự thường, giữ nguyên ký tự
            plain_text += cipher_text[i]
            
            # Di chuyển sang ký tự kế tiếp liền kề
            i += 1
            
    return plain_text


def main():
    
    print("=== CHƯƠNG TRÌNH KHÔI PHỤC VĂN BẢN GỐC ===")
    
    # Nhập dữ liệu chuỗi nén từ bàn phím
    cipher_input = input("Nhập chuỗi đã nén (cipher text): ")
    
    # Gọi hàm xử lý thuật toán giải nén chuỗi
    result = giai_nen_chuoi(cipher_input)
    
    # In kết quả khôi phục ra màn hình console
    print(f"-> Chuỗi gốc khôi phục (plain text): {result}")

if __name__ == "__main__":
    main()
