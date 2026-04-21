import re

S = input("Nhập chuỗi S: ").lower()
word = input("Nhập từ cần đếm: ").lower()

# Tách từ bỏ qua dấu câu
words = re.findall(r'\b\w+\b', S)

count = words.count(word)

print("Số từ", word, "là:", count)