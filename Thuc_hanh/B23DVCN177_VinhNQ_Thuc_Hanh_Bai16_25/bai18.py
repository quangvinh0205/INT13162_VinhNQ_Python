# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Bạn hãy viết chương trình tình tổng của 50 số chẵn bắt đầu từ 2.

# Khởi tạo 1 biến sum dùng để tính tổng 50 số chẵn
sum = 0

# Tạo 1 vòng lặp chạy từ 2 tới 102
for i in range (2, 102, 2):                     # Cấu trúc của vòng lặp for(số bắt đầu, số kết thúc, số bước nhảy)         
    sum+=i                                      #  Biến sum = sum + i trong đó ( sum sau dấu = là sum của giá trị cũ trước khi đã cộng với số i )

print("Tổng 50 số chẵn là:",sum)                # In ra màn hình khi có kết quả tổng 50 số chẵn. 
