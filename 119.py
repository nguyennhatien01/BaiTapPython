import math

# --- CÁC HÀM BỔ TRỢ ---

def is_prime(n):
    """Kiểm tra số nguyên tố tối ưu"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def rotate_standard(s):
    """Xoay chuỗi số 180 độ theo chuẩn cơ bản (0, 1, 6, 8, 9)
    Trả về chuỗi đã xoay hoặc None nếu chứa chữ số không hợp lệ"""
    mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    rev = []
    for char in reversed(s):
        if char not in mapping:
            return None
        rev.append(mapping[char])
    return "".join(rev)

def rotate_extended(s):
    """Xoay chuỗi số 180 độ theo chuẩn mở rộng (bổ sung thêm 2, 5)"""
    mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6', '2':'2', '5':'5'}
    rev = []
    for char in reversed(s):
        if char not in mapping:
            return None
        rev.append(mapping[char])
    return "".join(rev)

# --- GIẢI QUYẾT CÁC CÂU HỎI ---

LIMIT = 1000000

print("--- ĐANG XỬ LÝ DỮ LIỆU... ---")

results_a = []
results_b = []
results_c = []
results_d = []
results_e = []

for i in range(LIMIT):
    s = str(i)
    
    # Câu a & b: Strobogrammatic cơ bản
    rot_std = rotate_standard(s)
    is_stro_std = (rot_std == s)
    
    if is_stro_std:
        results_a.append(i)
        if is_prime(i):
            results_b.append(i)
            
    # Câu c & d: Strobogrammatic mở rộng
    rot_ext = rotate_extended(s)
    is_stro_ext = (rot_ext == s)
    
    if is_stro_ext:
        results_c.append(i)
        if is_prime(i):
            results_d.append(i)
            
    # Câu e: Không phải số stro, không phải số nguyên tố, nhưng xoay 180 độ là số nguyên tố
    if rot_std is not None and not is_stro_std and not is_prime(i):
        rotated_val = int(rot_std)
        if is_prime(rotated_val):
            results_e.append(i)

# --- IN KẾT QUẢ ---

print("\na.- Các số strobogrammatic nhỏ hơn 1 triệu:")
print(f"Có tất cả {len(results_a)} số.")

print("\nb.- Các số nguyên tố strobogrammatic nhỏ hơn 1 triệu:")
print(", ".join(map(str, results_b)))

print("\nc.- Các số strobogrammatic mở rộng nhỏ hơn 1 triệu:")
print(f"Có tất cả {len(results_c)} số.")

print("\nd.- Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu:")
print(", ".join(map(str, results_d)))

print("\ne.- Các số thỏa mãn điều kiện câu e:")
print(f"Có tất cả {len(results_e)} số. Một số số đầu tiên: {results_e[:20]}...")
