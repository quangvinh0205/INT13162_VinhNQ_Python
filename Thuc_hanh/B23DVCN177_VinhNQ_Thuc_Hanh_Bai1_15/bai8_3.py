# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python.
# Bạn hãy viết một chương trình giải phương trình trùng phương ax⁴+bx2+c=0.

# Import thư viện toán học và thư viện list
import math
from typing import List

# Cho hằng số Epsilon = 1e-9 để làm tròn số khi khoảng cách giữa một số với 0 là quá nhỏ và có thể chấp nhận được 
EPS = 1e-9

# Tạo 1 hàm riêng để dùng cho việc tính phương trình trùng phương
def gpttp(a,b,c):
# Xử lý trường hợp nếu a = 0 (trường hợp thoái hóa):
    if math.isclose(a,0.0,abs_tol=EPS):                                 # Nếu số a = 0 thì xét đến trường hợp tiếp theo (hàm math.isclose() dùng để so sánh 2 số thực, Cấu trúc của hàm math.isclose(a,b,*,rel_tol=1e-9,abs_tol=0.0)); 
                                                                        # TRONG ĐÓ [a số thứ nhất cần so sánh, b là số thứ 2, rel_tol = 1e-9 là sai số tương đối trong cấu trúc trên nó sẽ bằng 1e-9 là độ lệch cho phép giữa 2 số a và b, abs_tol = 0.0 là sai số TUYỆT ĐỐI chỉ dùng khi giá trị rất gần số 0 ]
        if math.isclose(b,0.0,abs_tol=EPS):                             # Nếu số b = 0 thì xét tiếp trường hợp tiếp theo 
            return None if math.isclose(c,0.0, abs_tol=EPS) else []     # Trả lại None nếu phương trình có vô số nghiệm, trả lại danh sách rỗng
        t=-c/b                                                          # Nếu b khác 0 thì thực hiện phương trình t 
        if math.isclose(t,0.0,abs_tol=EPS):                             # So sánh kết quả phương trình t với hàm số EPS
            return [0.0]                                                # Trả lại giá trị nếu điều kiện trên đúng
        elif t > EPS :                                                  # So sánh trường hợp nếu kết qua phương trình t lớn hơn hàm số EPS
            root = math.sqrt(t)                                         # Gán biến số root bằng căn bậc 2 của phương trình t 
            return [-root,root]                                         # Trả lại giá trị nếu điều kiện trên đúng
        else :
            return []                                                   # Trả lại danh sách rỗng mới nếu không thuộc những trường hợp trên

# Giải phương trình bậc 2 a*t^2 + b*t + c = 0
    delta = b * b - 4 * a * c                                           # Phương trình delta 
    if delta < -EPS:                                                    # Nếu delta nhỏ hơn tham số -EPS
        return []                                                       # Trả về danh sách rỗng mới
    t_value: List[float] = []                                           # Tạo 1 danh sách rỗng để chứa giá trị t
    if math.isclose(delta, 0.0, abs_tol=EPS):                           # So sánh giá trị delta = 0 thì sẽ có nghiệm kép
        t_value.append(-b/(2*a))                                        # Delta = 0 thì thực hiện phương trình (-b)/(2*a) và đưa vào vị trí cuối cùng trong danh sách 
    else:                                                               # Nếu delta lớn hơn 0 thì sẽ có 2 nghiệm phân biệt
        sqrt_dt = math.sqrt(delta)                                      # Tạo tham số sqrt_dt = căn bậc 2 của delta
        t_value.append((-b - sqrt_dt ) / (2*a))                         # Phương trình tính nghiệm đầu tiên rồi đưa vào cuối danh sách t
        t_value.append((-b + sqrt_dt ) / (2*a))                         # Phương trình tính nghiệm thứ 2 rồi đưa vào cuối danh sách t

# Tìm x từ 2 nghiệm t1 và t2
    raw_roots: List[float] = []                                         # Tạo 1 danh sách rỗng nghiệm gốc để chứa giá trị
    for t in t_value:                                                   # Duyệt từng giá trị trong danh sách t có chứa giá trị
        if math.isclose(t,0.0,abs_tol=EPS):                             # So sánh giá trị t với tham số EPS
            raw_roots.append(0.0)                                       # Nếu thỏa mãn thì thêm vào cuối danh sách raw_roots với giá trị là 0
        elif t > EPS:                                                   # Nếu giá trị t lớn hơn tham số EPS 
            root = math.sqrt(t)                                         # Gán tham số root thành biểu thức căn bậc 2 của t 
            raw_roots.extend([-root,root])                              # Nối tiếp ở cuối danh sách ( sự khác biệt giữa .append và .extend là [.append(x) chỉ khi x là 1 danh sách thì sẽ chuyển thành danh sách lồng danh sách ]; [.extend() là nối tiếp danh sách])
    
    if not raw_roots:                                                   # Nếu danh sách nghiệm gốc rỗng
        return []                                                       # Trả lại 1 danh sách rỗng mới  
    raw_roots.sort()                                                    # Sắp xếp lại danh sách nghiệm
    unique_roots: List[float] = [raw_roots[0]]                          # Khởi tạo 1 danh sách mới và lấy phần tử đầu tiên của danh sách nghiệm gốc1
    for r in raw_roots[1:]:                                             # Duyệt phần tử thứ 2 cho tới hết danh sách
        if not math.isclose(r, unique_roots[-1], abs_tol=EPS):          # Nếu phần tử cuối cùng của danh sách không trùng với nghiệm mới 
            unique_roots.append(r)                                      # Thêm nghiệm mới vào danh sách 

# Làm tròn những nghiệm có giá trị gần bằng với 0 trong phạm vi sai số là EPS
    return [0.0 if math.isclose(r, 0.0, abs_tol = EPS ) else r for r in unique_roots]

# Nhập lần lượt số a,b,c từ bàn phím
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

# In kết quả nghiệm ra màn hình 
print("Kết quả nghiệm",gpttp(a,b,c))
