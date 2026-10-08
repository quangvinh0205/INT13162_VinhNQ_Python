# Name : VinhNQ
# Date : 08/10/2026
# Mô tả yêu cầu: Cho một danh sách số. Viết chương trình đếm các số nguyên tố có trong danh sách.

# Import thư viện math
import math

# Tạo hàm riêng dùng để kiểm tra số nguyên tố
def snt(a):
    if a < 2:                               # Số nguyên tố phải lớn hơn 1
        return False
    for i in range(2,int(math.sqrt(a))+1):       # Chạy vòng lặp từ 2 tới căn bậc 2 của a, nếu có giá trị thỏa mãn thì trả về Flase
        if a % i == 0:
            return False
    return True                             # Nếu không có giá trị nào thỏa mãn trong vòng lặp thì trả về giá trị True

# Tạo 1 danh sách chứa các số và danh sách rỗng
dss = [64,73,4,2,46,53,54,7,87,90,42,22,97,88]
dsr = []

# Chạy 1 vòng lặp trong danh sách số đã cho
for i in dss:
    if snt(i):                              # Nếu hàm trả về giá trị True thì thêm phần tử đó vào cuối danh sánh 
        dsr.append(i)

csnt = len(dsr)                             # Sử dụng len() để đếm các phần tử ở trong danh sách

# In ra màn hình kết quả 
print(f"Có {csnt} số nguyên tố trong danh sách")
print("Các số nguyên tố ở trong danh sách:",dsr)
