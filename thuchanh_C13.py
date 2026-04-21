import re

# Nhập chuỗi nhiều dòng (kết thúc bằng dòng rỗng)
print("Nhập chuỗi (Enter 2 lần để kết thúc):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Xử lý từng dòng
result = []
for line in lines:
    line = line.strip()  # bỏ khoảng trắng đầu cuối dòng
    line = re.sub(r'\s+', ' ', line)  # nhiều khoảng trắng -> 1 khoảng trắng
    line = re.sub(r'\s+([.,])', r'\1', line)  # bỏ khoảng trắng trước . ,
    result.append(line)

# In kết quả
print("\nChuỗi hoàn chỉnh:")
for line in result:
    print(line)