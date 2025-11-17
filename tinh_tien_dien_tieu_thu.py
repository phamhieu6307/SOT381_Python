kwh = int(input("nhập số điện tiêu thụ(kwh): "))
if kwh <= 50 :
    money = kwh * 1678
elif kwh <= 100 :
    money = 50 * 1678 + (kwh - 50) * 1734
elif kwh <= 200 :
    money = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
elif kwh <= 350 :
    money = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 150) * 2536
else:
    money = 50 * 1678 + 50 * 1734 + 100 * 2014 + 150 * 2536 + (kwh - 350) * 2927
print("tiền điện phải trả là : " , money , "VND")