number = int(input("Nhập số cần kiểm tra: "))
n = 1
for i in range(1, number + 1):
    n *= i
print("Kết quả:", n)
