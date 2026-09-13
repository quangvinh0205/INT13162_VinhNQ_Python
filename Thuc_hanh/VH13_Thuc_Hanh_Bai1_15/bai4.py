# Name : VinhNQ
# Date : 13/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Nhập 2 số a, b từ bàn phím. Ví dụ nhập 2 số a=5, b=10. 
# Hãy đổi giá trị (hoán vị) 2 số a b cho nhau sao cho kết quả là: a=10, b=5.

# Nhập 2 số a và b từ bàn phím 
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

# Hoán vị giá trị 2 biến
a,b=b,a         # Giá trị biến a thành giá trị biến b và ngược lại 

# In ra màn hình sau khi hoán vị
print("số a sau khi hoán vị giá trị là",a)
print("Số b sau khi hoán vị giá trị là ",b)
