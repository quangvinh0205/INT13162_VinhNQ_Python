# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu:  Sử dụng ngôn ngữ lập trình Python. Bạn hãy viết chương trình tính tổng của 50 số 100, 99, 98, …51.

# Khởi tạo biến sum dùng để tính tổng
sum = 0 

# Chạy vòng lặp for từ 100 tới 51
for i in range(100,50,-1):                              # Cấu trúc của vòng lặp for(số bắt đầu, số kết thúc, số bước nhảy)        
    sum += i                                            # Biến sum = sum + i trong đó ( sum sau dấu = là sum của giá trị cũ trước khi đã cộng với số i )

print("Tổng 50 số từ 100 tới 51 là: ",sum)              # In ra màn hình kết quả khi đã tính xong tổng số