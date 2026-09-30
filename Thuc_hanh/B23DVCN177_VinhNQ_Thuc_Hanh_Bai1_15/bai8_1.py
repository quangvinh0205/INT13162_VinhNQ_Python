# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. 
# Bạn hãy viết một chương trình giải phương trình bậc nhất ax+b=0.
# ❖ Bạn hãy viết một chương trình giải phương trình bậc hai ax2+bx+c=0.
# ❖ Bạn hãy viết một chương trình giải phương trình trùng phương ax⁴+bx2+c=0.
# ❖ Bạn hãy viết một chương trình giải hệ phương trình bậc nhất hai ẩn


# Nhập 2 số a và b 
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

# Xét trường hợp
if a != 0:                                          # Nếu a khác 0 thì sẽ thực hiện phương trình bên dưới rồi in ra nghiệm
    x = -(b / a)
    print("Nghiệm của phương trình là: ",round(x,2))
elif a == 0 and b == 0:                             # Nếu a bằng 0 và b bằng 0 thì phương trình có vô số nghiệm
    print("Phương trình có vô số nghiệm !")
elif a == 0 and b!= 0:                              # Nếu a bằng 0 và b khác 0 thì phương trình vô nghiệm 
    print("Phương trình vô nghiệm !")
