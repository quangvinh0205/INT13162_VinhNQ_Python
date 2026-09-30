# Name : VinhNQ
# Date : 13/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Nhập một số N bất kỳ từ bàn phím.
# ❖ N có phải số nguyên không? In thông báo ra màn hình.
# ❖ Kiểm tra tính chẵn lẻ của N. In kết quả ra màn hình.
# ❖ N có phải là số chẵn dương không? In thông báo ra màn hình.
# ❖ N có phải là số lẻ âm không? In thông báo ra màn hình.
# ❖ N có phải số chính phương không? In thông báo ra màn hình.
# ❖ Nếu 0<N<1000 thì kiểm tra xem N có phải số đặc biệt không?
# (số đặc biệt là số nguyên có tổng lập phương của các ký số bằng chính nó, ví dụ số 153 = 13 + 53 + 33).

# Import thư viện toán để sử dụng kiểm tra số chính phương
import math


# Nhập một số N bất kỳ từ bàn phím:
n = int (input("Nhập một số n bạn muốn: "))

# Kiểm tra N là số nguyên:
if isinstance(n, int):                    # Hàm isinstance() dùng để kiểm tra dữ liệu có phải là số nguyên hay không [Cú pháp: isinstance(bien_can_kiem_tra, int)]
    print(n,"là số nguyên")             # Nếu thỏa mãn điều kiện ở trên thì in ra màn hình 
else:                                   # Không thỏa mãn thì sẽ in ra màn hình 
    print(n,"không phải là số nguyên")

# Kiểm tra tính chẵn lẻ của N:
if n % 2 == 0 : print(n,"là số chẵn ")    # Nếu n chia hết cho 2 là số chẵn
elif n % 2 !=0 : print(n,"là số lẻ!")     # Nếu n không chia hết cho 2 là số lẻ
elif n == 0 : print(n,"là số 0")           # Nếu n bằng 0 thì in ra màn hình

# Kiểm tra số N là số chẵn dương, lẻ âm:
if n % 2 == 0 and n > 0: print (n, "là số chẵn dương!")               # Nếu N chia hết cho 2 và lớn hơn 0 thì in ra màn hình
elif  n % 2 == 0 and n < 0: print(n, " à số lẻ âm!")                  # Nếu N không chia hết cho 2 và nhỏ hơn 0 thì in ra màn hình

# Kiểm tra số chính phương:
if n > 0:                                                                   # Nếu N lớn hơn 0 thì thực hiện khối lệnh bên dưới
    if math.isqrt(n) ** 2 == n: print(n, " là số chính phương!")            # Nếu căn bậc 2 của N bình phương lên bằng số N thì in ra màn hình
    else: print(n, "không phải là số chính phương !")                       # Nếu không thì in ra màn hình
else: print(n, "là số âm không thế là số chính phương")                     # Nếu N nhỏ hơn 0 thì in ra màn hình

# Kiểm tra số lập phương: 
while not(0 < n and n < 1000): n = int(input("Nhập lại số: "))          # Nếu số N không thuộc trong khoảng từ 0 đến dưới 1000 thì nhập lại
cube_root = round (n ** (1/3))                                          # Đặt 1 biến lấy căn bậc 3 của số n 
if cube_root ** 3  == n: print(n,"là số lập phương!")                 # Kiểm tra biến vừa lưu trữ kết quả khi mũ 3 lên bằng số N thì in ra màn hình 
else: print(n, "không phải là số lập phương!")                        # Nếu không thỏa mãn điều kiện thì in ra màn hình 
