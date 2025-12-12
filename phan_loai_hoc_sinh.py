diem_so = [ 8.5 , 7.0 , 9.2 , 6.8 , 5.5 , 8.8 ]
for diem in diem_so :
    if diem>=8:
        xep_loai = "giỏi"
    elif 6.5<=diem<8:
        xep_loai = "khá"
    else:
        xep_loai = "trung bình"
    print(f"điểm {diem} {xep_loai}")