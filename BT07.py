a = int(input("Nhập số cần kiểm tra: "))
b = int(input("Nhập số cần kiểm tra: "))
for i in range(a,b,1):
    if i > 2: 
        for j in range (2,i-1,1):
            if i % j != 0:
                print("Number: ", i)
