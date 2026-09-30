# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Bạn hãy viết chương trình tính tổng của 50 số 1, 2, 3, …, 50.

# Khởi tạo 1 biến sum bằng 0 dùng để tính tổng các số
sum = 0

# Dùng vòng lặp for chạy từ 1 tới 50 để tính tổng các số
for i in range (1,51):
    sum += i                                        # Biến sum = sum + i trong đó ( sum sau dấu = là sum của giá trị cũ trước khi đã cộng với số i )

print("Tổng 50 số từ 1 tới 50 là: ",sum)            # In ra màn hình kết quả khi đã tính xong tổng số