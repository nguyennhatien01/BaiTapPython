import math

def kiemtrasnt(k):
    # kiểm tra xem k có phải là số nguyên tố hay không 
    if k < 2:
        return False
    # kiểm tra xem các ước số của k
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True


#--------------------------------------------------------------------------------
def bangcuuchuong():
    print("\n--In bảng cửu chương--")
    # nhập a, b (cách nhau bởi dấu phẩy)
    chuoinhap = input("Nhập a, b (cách nhau bởi dấu phẩy): ")
    # sử dụng hàm map() để chuyển đổi chuỗi nhập vào thành 2 số nguyên a và b
    a, b = map(int, chuoinhap.split(","))
    
    # xác định số nhỏ nhất và số lớn nhất
    start = min(a, b)
    end = max(a, b)
    
    for i in range(start, end + 1):
        print(f"\n[Bảng cửu chương {i}]")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
            
            
#---------------------------------------------------------------------------------         
def sntnhohonn():
    print("\n---Liệt kê snt nhỏ hơn n")
    n = int(input("Nhập số nguyên dương n: "))
    
    # tạo danh sách các snt nhỏ hơn n
    danhsachsnt = []
    for i in range(2, n):
        if kiemtrasnt(i):
            danhsachsnt.append(str(i))
            
    # in danh sách các snt nhỏ hơn n, join() dùng để nối các phần tử trong danh sách
    print(f"Các số nguyên tố < {n}: {', '.join(danhsachsnt)}")
    
    
#----------------------------------------------------------------------------------
def uocsonguyento():
    print("\n---Ước số nguyên tố---")
    n = int(input("Nhập số nguyên dương n: "))
    
    danhsachuocsnt = []
    # tìm ước snt của n
    for i in range(2, n + 1):
        # đk: i là ước của n và i là snt
        if n % i == 0 and kiemtrasnt(i):
            danhsachuocsnt.append(str(i))
            
    print(f"Các số vừa là ước số của {n}, vừa là số nguyên tố: {', '.join(danhsachuocsnt)}")



# hàm main   
if __name__ == "__main__":
    bangcuuchuong()
    sntnhohonn()
    uocsonguyento()