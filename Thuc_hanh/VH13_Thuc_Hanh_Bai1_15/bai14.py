# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python.
# ❖ In ra các số từ 1 đến 100.
# ❖ In ra các số từ 100 đến 1

# Tạo một danh sách rỗng để chứa các số từ 1 tới 100
mang=[]

# Cho số chạy từ 1 tới 100 với mỗi bước chạy là 1
for i in range (1, 101, 1) : 
    mang.append(i)              # Đẩy số i vào cuối danh sách đã tạo trước đó 
    print(i, end=", ")           # In ra màn hình số i chạy từ 1 tới 100 

print("\n \n")

mang.reverse()                  # Đảo ngược lại danh sách
print(mang)                     # In ra màn hình danh sách đã đảo