# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python.
# ❖ In ra các số từ 1 đến 100 mà chia hết cho 3.
# ❖ In ra các số từ 99 đến 1 mà chia hết cho 7.

# Tạo danh sách rỗng để chứa các số từ 1 tới 100
ds = []

# Tạo vòng lặp chạy từ 1 tới 100 với mỗi bước là 1
for i in range (1, 100, 1):
    if i % 7 == 0 : ds.append(i)            # Nếu i chia hết cho 7 thì xếp vào cuối danh sách
    if i % 3 == 0 : print(i, end=", ")      # Nếu i chia hết cho 3 thì in ra màn hình 

print("\n")             # Tạo 1 khoảng cách dòng

ds.reverse()            # Đảo ngược danh sách
print(ds)               # In ra các số chia hết cho 7 từ 99 đến 1 