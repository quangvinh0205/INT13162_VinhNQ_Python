# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình …. Cho hai số A và B là hai số nguyên dương và A phải nhỏ hơn B (0 < A < B < 100). Hãy viết chương trình cho phép nhập hai
# số A và B đó từ bàn phím và thực hiện:
# ❖ Tìm các số nguyên tố từ A đến B.
# ❖ Tìm ước chung lớn nhất của A và B.

# Import thư viện toán
import math

# Nhập 2 số A, B từ bàn phím 
a = int(input("Nhập số A:"))
b = int(input("Nhập số B:"))
while a > b and b > 100 and a < 0:                                  # Tạo vòng lặp nếu số a lớn hơn số b, số b lớn hơn 100 và số a nhỏ hơn 0 thì nhập lại 
    a = int(input("Nhập lại số A:"))
    b = int(input("Nhập lại số B:"))

# Tạo hàm kiểm tra số nguyên tố
def ktsnt(n):
    if n < 2:                                                       # Nếu số n nhỏ hơn 2 thì trả lại giá trị Flase
        return False
    for i in range (2, int(math.sqrt(n))+1):                        # Chạy vòng lặp từ 2 cho tới căn bậc 2 của n
        if n % i == 0:                                              # Nếu số n chia hết cho i thì trả về giá trị Flase
            return False
    return True                                                     # Nếu vòng lặp trên không tìm thấy số n có thể chia hết thì trả về giá trị True

# Tạo hàm xác định số nguyên tố 
def xdsnt(a,b):
    ds = []                                                         # Khởi tạo 1 danh sách rỗng
    for so in range (a,b +1):                                       # Tạo 1 vòng lặp chạy từ a tới b để duyệt từng số
        if ktsnt(so):                                               # Nếu số chạy từ a đến b được hàm kiểm tra sô nguyên tố (ktsnt) thì thêm vào cuối danh sách
            ds.append(so)
    return ds                                                       # Khi đã chạy xong thì trả lại toàn bộ mảng các số nguyên tố đã tìm ra

# Tạo biến kết quả để lưu các số nguyên tố đã tìm được
kq = xdsnt(a,b)

# Tạo hàm tìm ước chung lớn nhất của a và b
ucln = math.gcd(a,b)

# In ra màn hình
print(f"Ước chung lớn nhất của 2 số {a} và {b} là: {ucln}")         # In ra ước chung lớn nhất của 2 số a và b 
print(f"Các số nguyên tố từ {a} đến {b} là: {kq}")                  # In ra chuỗi định dạng (f-string) ra màn hình và tự động điền các giá trị của biến a,b đã có và mảng kq 
