# Name : VinhNQ
# Date : 13/09/2026
# Mô tả yêu cầu:  Sử dụng ngôn ngữ lập trình Python. Hãy nhập vào lương và giờ làm việctrong tháng của 1 nhân viên,
# sau đó xác định thưởng của của nhân viên đó theo quy định sau:
# ❖ Nếu giờ làm việc > =200 thì thưởng =20% lương.
# ❖ Nếu giờ làm việc > = 100 và <200 thì thưởng = 10% lương.
# ❖ Những trường hợp khác thì thưởng =0.

# Nhập vào lương và giờ làm việc của nhân viên 
luong = int(input("Nhập lương của nhân viên: ")) 
time = int(input("Nhập số giờ làm việc của nhân viên: "))

# Xác định thưởng của nhân viên theo quy định 
if time >= 200: thuong = 0.2 * luong                            # Nếu giờ làm việc >= 200 thì thưởng = 20% lương
elif time >=100 and time < 200 : thuong = 0.1 * luong            # Nếu giờ làm việc >= 100 và < 200 thì thưởng = 10% lương
else: thuong = 0                                                # Những trường hợp khác thì thưởng = 0.

# In ra kết quả thưởng của nhân viên
print("Thưởng của nhân viên là: ", thuong)
