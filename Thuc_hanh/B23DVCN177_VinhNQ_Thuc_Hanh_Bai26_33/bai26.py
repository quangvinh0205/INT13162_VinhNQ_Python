# Name : VinhNQ
# Date : 4/10/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Viết chương trình tính tổng nghịch đảo của N số nguyên đầu tiên theo công thức: S = 1 + 1/2 + 1/3 + ... + 1/N

# Nhập số N từ bàn phím
n = int(input("Nhập số N:"))

# Tạo 1 biến sum = 1 
sum = 1

# Khởi tạo vòng lặp for chạy từ 1 tới n
for i in range (2,n + 1):
    sum += (1/i)                            # Theo công thức đề bài sẽ cộng dồn giá trị của mỗi giá trị khi đã tính xong vào biến sum

# In ra màn hình sau khi chạy xong vòng lặp
print(f"Tổng nghịch đảo của N số nguyên đầu tiên là: {sum:.2f} ")
