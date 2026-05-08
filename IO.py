# Mở file
file = open("baitap.txt", "r", encoding="utf-8")
# Đọc nội dung
text = file.read()
# Đóng file
file.close()
# In nội dung
print(text)




# Tách các từ
words = text.split()
print(words)




# Danh sách từ duy nhất
dictionary = []
# Vị trí xuất hiện
positions = []




# Duyệt từng từ
for word in words:
    # Nếu từ chưa có
    if word not in dictionary:
        dictionary.append(word)
    # Lưu vị trí index
    positions.append(dictionary.index(word))
    
    
    
    
# In dữ liệu nén
print(dictionary)
print(positions)




# Mở file nén để ghi
compressed = open("compressed.txt", "w", encoding="utf-8")
compressed.write("DICTIONARY\n")
for word in dictionary:
    compressed.write(word + "\n")
compressed.write("POSITIONS\n")
for pos in positions:
    compressed.write(str(pos) + " ")
compressed.close()




# Mở file nén để đọc
compressed = open("compressed.txt", "r", encoding="utf-8")
lines = compressed.readlines()
compressed.close()





#Tạo biến giải nén 
dictionary = []
positions = []
mode = ""




# Tách dữ liệu
for line in lines:
    line = line.strip()
    if line == "DICTIONARY":
        mode = "dictionary"
        continue
    elif line == "POSITIONS":
        mode = "positions"
        continue
    if mode == "dictionary":
        dictionary.append(line)
    elif mode == "positions":
        positions = line.split()
        
        
        
        
# Khôi phục văn bản
restored_text = ""
for pos in positions:
    restored_text += dictionary[int(pos)] + " "




# Ghi file đã khôi phục
restored = open("restored.txt", "w", encoding="utf-8")
restored.write(restored_text)
restored.close()




# In kết quả
print(restored_text) # In ra văn bản đã khôi phục