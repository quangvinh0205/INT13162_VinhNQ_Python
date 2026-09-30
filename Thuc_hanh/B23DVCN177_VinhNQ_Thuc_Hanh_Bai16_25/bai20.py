# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Bạn hãy viết chương trình tính tổng của 20 số 5, 10, 15, ..., 100.

# Khởi tạo 1 biến sum dùng để tính tổng 50 số lẻ
sum = 0

# Tạo 1 vòng lặp chạy từ 5 tới 105
for i in range (5, 105, 5):                     # Cấu trúc của vòng lặp for(số bắt đầu, số kết thúc, số bước nhảy)         
    sum+=i                                      #  Biến sum = sum + i trong đó ( sum sau dấu = là sum của giá trị cũ trước khi đã cộng với số i )

print("Tổng 50 số lẻ là:",sum)                  # In ra màn hình khi có kết quả tổng 50 số lẻ. 