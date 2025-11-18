numberInt = int(input("Nhập 1 số nguyên: "))
count = 0

for i in range(1, numberInt + 1):
    count += i

print("Tổng các số nguyên dương đến N là:", count)
