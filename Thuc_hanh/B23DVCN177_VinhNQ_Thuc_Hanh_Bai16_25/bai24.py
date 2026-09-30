# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Viết chương trình nhập vào một số nguyên dương N và thực hiện:
# ❖ Số nguyên dương N có bao nhiêu chữ số?
# ❖ Tính tổng các chữ số của N.
# ❖ In ra chữ số lớn nhất của N.

# Nhập số n từ bàn phím
n = int(input("Nhập số N: "))
while n < 0:                                # Nếu n là số âm thì yêu cầu nhập lại
    n = int(input("Nhập lại số N: "))

temp = n                                    # Khởi tạo 1 biến tạm bằng số n
sum = 0                                     # Tạo 1 biến sum dùng để cộng các số trong số n 
scs = len(str(n))                           # Chuyển số n qua sang chuỗi để đếm số chữ số
sln = max(str(abs(n)))                      # Chuyển số n qua dạng chuỗi ký tự rồi dùng hàm max() để tìm ký tự chữ số có giá trị lớn nhất trong chuỗi đó
while temp > 0:                             # Cho vòng lặp chạy với điều kiện là biến tạm (temp) lớn hơn 0
    m = temp % 10                           # Biến m lưu giá trị dư khi biến tạm chia cho 10  
    sum += m                                # Biến sum dùng để cộng giá trị dư 
    temp //=10                              # Biến temp chia lấy phần nguyên 

# In ra màn hình các kết quả
print("Số chữ số của số N là:",scs)
print("Tổng chữ số N là:",sum)
print("Số lớn nhất của số N là:",sln)