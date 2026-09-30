# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Bạn hãy viết chương trình nhập n từ bàn phím và tính n! (n!= 1*2*3*...*n)

# Nhập số N từ bàn phím
n = int(input("Nhập số N: "))

# Khởi tạo biến sum với giá trị băng 1 vì nếu bằng 0 khi tính giai thừa sẽ luôn trả về giá trị là 0
sum = 1

# Chạy vòng lặp for từ 1 cho tới n+1
for i in range(1,n+1,1):                        # Cấu trúc của vòng lặp for(số bắt đầu, số kết thúc, số bước nhảy)
    sum *= i                                    #  Biến sum = sum * i trong đó ( sum sau dấu = là sum của giá trị cũ trước khi đã nhân với số i )

print("Giai thừa của số",n,"là:",sum)           # In ra màn hình khi có kết quả của giai thừa số n