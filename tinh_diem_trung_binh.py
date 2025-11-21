name = input("nhập tên học sinh : ")
toán = float(input("nhập điểm toán : "))
lý = float(input("nhập điểm lý : "))
hóa = float(input("nhập điểm hóa : "))
điểm_trung_bình = ( toán + lý + hóa ) / 3
if điểm_trung_bình >= 8 :
    xếp_loại = "Giỏi"
elif điểm_trung_bình >= 6.5 :
    xếp_loại = "Khá"
elif điểm_trung_bình >= 5 :
    xếp_loại = "Trung Bình"
else :
    xếp_loại ="yếu"
print("KẾT QUẢ HỌC TẬP")
print(f"Họ và tên :{name}")
print(f"Điểm toán :{toán}")
print(f"Điểm lý :{lý}")
print(f"Điểm hóa :{hóa}")
print(f"điểm trung bình :{điểm_trung_bình:.2f}")
print(f"xếp loại :{xếp_loại}")