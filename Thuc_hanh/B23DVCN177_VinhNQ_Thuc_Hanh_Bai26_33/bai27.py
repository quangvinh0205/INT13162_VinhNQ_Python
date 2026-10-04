# Name : VinhNQ
# Date : 04/10/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Viết chương trình nhập N từ bàn tính và tính tổng bình phương các số lẻ từ 1 đến N

# Nhập số N từ bàn phím
n = int(input("Nhập số n: "))

# Tạo 1 biến sum = 0 để lưu giá trị khi tính tổng
sum = 0

# Tạo vòng lặp chạy từ 1 tới N với bước nhảy là 2 vì sau 1 số lẻ là 1 số chẵn 
for i in range (1,n+1,2):
        sum += (i**2)                               # Lưu giá trị khi thực hiện xong biểu thức

# In ra màn hình
print("Tổng bình phương các số lẻ là: ",sum)