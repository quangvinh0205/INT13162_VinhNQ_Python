# Name : VinhNQ
# Date : 04/10/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Viết chương trình vẽ hình chữ nhật rỗng bằng các dấu *

# Nhập chiều dài và chiều rộng từ bàn phím
cr = int(input("Nhập chiều rộng: "))
cd = int(input("Nhập chiều dài: "))

#Tạo vòng lặp đầu tiên để vẽ chiều dài của 
for i in range (1,cd+1):
    for j in range (1,cr+1):
        if i == 1 or i == cd or j == 1 or j == cr:
            print("*",end="")
        else:
            print(" ",end="")
    print()