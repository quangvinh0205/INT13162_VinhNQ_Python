# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. 
# Hãy nhập vào năm sản xuất của một chiếc máy tính, sau đó đưa ra đề xuất đối với máy tính đó theo quy tắc sau:
# ❖ Nếu năm sản xuất >=15 thì đưa ra đề xuất "Thay the"
# ❖ Nếu năm sản xuất >=10 và <15 thì đưa ra đề xuất "Bao tri"

# Nhập năm sản xuất của máy tính
nsx = input("Nhập năm sản xuất: ")

#Xét điều kiện 
if 2026 - nsx >= 15 : print("Thay The")                                 # Nếu số năm trên 15 năm thì in ra màn hình 
elif 2026 - nsx >= 10 and 2026 - nsx < 15 : print("Bao tri")            # Nếu số năm trên 10 năm và dưới 15 năm thì in ra màn hình
else: print("Khong co de xuat")                                         # Nếu là những trường hợp khác thì in ra màn hình