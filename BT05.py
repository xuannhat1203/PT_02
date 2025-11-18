number = int(input("Nhập số cần kiểm tra: "))

original = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number //= 10

if original == reverse_number:
    print("Đây là số đối xứng!")
else:
    print("Không phải số đối xứng.")
