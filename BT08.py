a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Đây là 3 cạnh của tam giác")
else:
    print("Đây không phải 3 cạnh của tam giác")
