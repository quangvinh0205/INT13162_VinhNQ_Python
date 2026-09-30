# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Bạn hãy nhập vào một số N bất kỳ và kiểm tra xem N có phải số nguyên tố hay không?
# (Số nguyên tố là một số nguyên dương lớn hơn 1 và chỉ chia hết cho 1 và chính nó, ví dụ: 2, 3, 5, 7, 11, ...)

# Nhập số N từ bàn phím
n = int(input("Nhập số N: "))
while n < 0:                                        # Nếu số n nhỏ hơn 0 thì yêu cầu nhập lại 
    n = int(input("Nhập lại số N: "))

# Tạo 1 biến đếm bằng 0
count = 0

# Khởi tạo 1 vòng lặp for chạy từ 1 cho tới n
for i in range(1,n+1,1):                            # Cấu trúc của vòng lặp for(số bắt đầu, số kết thúc, số bước nhảy)
    if n % i !=0:                                   # Nếu số n không chia hết cho i thì không tăng biến đếm (count)
        count+=0
    else:                                           # Nếu số n chia hết cho i thì tăng biến đếm (count) lên 1
        count+=1

if count == 2:                                      # Nếu biến đếm bằng 2 thì đấy là số nguyên tố (vì chỉ có số 1 và chính số đó chia hết )      
    print(n, "Là số nguyên tố")
else:                                               # Nếu biến đếm dưới hoặc trên 2 thì không phải là số nguyên tố
    print(n, "Không phải số nguyên tố")
    