# Name : VinhNQ
# Date : 04/10/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Viết chương trình vẽ một tam giác cân rỗng bằng các dấu *

# Nhập chiều cao của tam giác cân từ bàn phím
n = int(input("Nhập chiều cao của tam giác: "))

# Tạo vòng lặp đầu tiên dùng để tạo khoảng trắng 
for i in range (1, n + 1):
    # Tạo khoảng trắng ở bên trái
    print(" " * (n - i), end="")
    # Tạo vòng lặp thứ 2 lồng vào vòng lặp trên để in dấu *
    for j in range (1, 2 * i):
        # Nếu j bằng 1 thì in dấu * ở cạnh bên trái, 
        # Nếu j bằng 2 * i - 1 thì in dấu * ở cạnh bên phải, 
        # Nếu i bằng n thì in toàn bộ là dấu *
        if j == 1 or j == 2 * i - 1 or i == n:               
            print("*",end="")
        # Nếu không thuộc điều kiện trên thì in khoảng trắng
        else:
            print(" ",end="")
    # Xuống dòng sau khi đã in hết 1 hàng
    print()

