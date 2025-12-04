P = float(input("Nhập số tiền ban đầu: "))
r = float(input("Nhập lãi suất hàng năm (%): ")) / 100
n = int(input("Nhập số năm gửi: "))

A = P * (1 + r) ** n

print(f"Số tiền nhận được sau {n} năm là: {A:.2f} VND")
