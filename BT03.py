numberInt = int(input("Nhập 1 số nguyên: "))

if numberInt % 15 == 0:
    print("Số vừa nhập chia hết cho cả 3 và 5")
elif numberInt % 3 == 0:
    print("Số vừa nhập chia hết cho 3")
elif numberInt % 5 == 0:
    print("Số vừa nhập chia hết cho 5")
else:
    print("Số vừa nhập không chia hết cho 3, 5 hoặc 15")
