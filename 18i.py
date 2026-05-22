# 1. Định nghĩa hàm lambda kiểm tra số Palindrome
is_palindrome = lambda n: str(n) == str(n)[::-1]

# 2. In 30 số thập phân palindrome đầu tiên để kiểm chứng kết quả theo đề bài
print("30 số palindrome đầu tiên:")
count = 0
for i in range(0, 1000001):  # Bắt đầu từ 0 theo ví dụ của đề
    if is_palindrome(i):
        print(i, end=" ")
        count += 1
        if count >= 30:
            break
print("\n")
