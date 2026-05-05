def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Nhập danh sách
numbers = []

while True:
    try:
        x = int(input("Nhập số nguyên: "))
        numbers.append(x)
    except:
        print("Vui lòng nhập số hợp lệ!")
        continue

    choice = input("Bạn có muốn nhập tiếp không? (Y/N): ").strip().upper()
    if choice == 'N':
        break

# a) In số nguyên tố
primes = [n for n in numbers if is_prime(n)]
print("\nCác số nguyên tố trong list:", primes)

# b) Trung bình cộng số âm và số dương
pos = [n for n in numbers if n > 0]
neg = [n for n in numbers if n < 0]

if pos:
    print("Trung bình số dương:", sum(pos) / len(pos))
else:
    print("Không có số dương")

if neg:
    print("Trung bình số âm:", sum(neg) / len(neg))
else:
    print("Không có số âm")

# c) Max, Min
if numbers:
    print("Số lớn nhất:", max(numbers))
    print("Số nhỏ nhất:", min(numbers))

# d) Kiểm tra tăng dần
is_increasing = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))

if is_increasing:
    print("Danh sách đã được sắp xếp tăng dần")
else:
    print("Danh sách chưa được sắp xếp tăng dần")