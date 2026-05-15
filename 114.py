def dao_nguoc(n):
    return int(str(n)[::-1])


def uscln(a, b):

    while b != 0:
        a, b = b, a % b

    return a


def la_so_than_thien(n):

    so_dao = dao_nguoc(n)

    return uscln(n, so_dao) == 1


a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

count = 0

print("Cac so than thien:")

for i in range(a, b + 1):

    if la_so_than_thien(i):
        print(i, end=" ")
        count += 1

print("\nSo luong:", count)