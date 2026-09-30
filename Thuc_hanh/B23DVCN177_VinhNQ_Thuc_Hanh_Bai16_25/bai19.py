# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Bạn hãy viết chương trình tình tổng của 50 số lẻ bắt đầu từ 1.

# Khởi tạo 1 biến sum dùng để tính tổng 50 số lẻ
sum = 0

# Tạo 1 vòng lặp chạy từ 1 tới 101
for i in range (1, 101, 2):                     # Cấu trúc của vòng lặp for(số bắt đầu, số kết thúc, số bước nhảy)         
    sum+=i                                      #  Biến sum = sum + i trong đó ( sum sau dấu = là sum của giá trị cũ trước khi đã cộng với số i )

print("Tổng 50 số lẻ là:",sum)                # In ra màn hình khi có kết quả tổng 50 số lẻ. 
