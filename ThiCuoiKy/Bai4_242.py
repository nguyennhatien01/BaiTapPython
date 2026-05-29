# Số đồng nhất - cách 1
sodongnhatall = lambda x: all(c == str(x)[0] for c in str(x))


# số đồng nhất - cách 2
sodongnhatany = lambda x: not any(c != str(x)[0] for c in str(x))


# số hoàn thiện
sohoanthien = lambda n: sum(i for i in range(1, n) if n % i == 0) == n if n > 1 else False



# giới hạn 1-10000
khoang = range(1, 10001)

print("---Số đồng nhất (dùng all)---")
dsdongnhatall = [str(x) for x in khoang if sodongnhatall(x)]
print(", ".join(dsdongnhatall))

print("\n---Số đồng nhất (dùng any)---")
dsdongnhatany = [str(x) for x in khoang if sodongnhatany(x)]
print(", ".join(dsdongnhatany))

print("\n---Số hoàn thiện trong khoảng 1 - 10000---")
dshoanthien = [str(x) for x in khoang if sohoanthien(x)]
print(", ".join(dshoanthien))
