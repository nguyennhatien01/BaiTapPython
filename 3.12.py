from collections import Counter

# Nhập chuỗi
S1 = input("Nhập chuỗi S1: ")
S2 = input("Nhập chuỗi S2: ")

# Đưa về Counter
c1 = Counter(S1)
c2 = Counter(S2)

# a) Ký tự xuất hiện trong cả 2 chuỗi
common = c1 & c2
print("\na) Ký tự xuất hiện trong cả 2 chuỗi:")
print(list(common.keys()))

# b) Đếm ký tự riêng biệt
only_s1 = set(S1) - set(S2)
only_s2 = set(S2) - set(S1)

print("\nb) Số ký tự chỉ có trong S1:", len(only_s1))
print("Số ký tự chỉ có trong S2:", len(only_s2))

# c) In các ký tự riêng biệt
print("\nc) Ký tự có trong S1 nhưng không có trong S2:")
print(list(only_s1))

print("Ký tự có trong S2 nhưng không có trong S1:")
print(list(only_s2))