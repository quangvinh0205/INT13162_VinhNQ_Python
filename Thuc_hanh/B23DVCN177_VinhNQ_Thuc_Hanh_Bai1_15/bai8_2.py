# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python.
# Bạn hãy viết một chương trình giải phương trình bậc hai ax2+bx+c=0.

import math

# Nhập 3 số a, b, c 
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

delta = b**2 - 4*(a*c)          # Dùng công thức tính delta tìm ra trường hợp tính nghiệm

if delta < 0: print("Phương trình vô nghiệm !")                     # Nếu delta nhỏ hơn 0 thì pt vô nghiệm
elif delta > 0:                                                     # Nếu delta lớn hơn 0 thì pt có 2 nghiệm phân biệt
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b - math.sqrt(delta)) / 2*a
    print("Phương trình có 2 nghiệm kép lần lượt là: ",x1 ,x2)
elif delta == 0:                                                    # Nếu delta bằng 0 thì phương trình có nghiệm kép
    x = (-b) / 2*a
    print("Phương trình có nghiệm kép là: ",x)