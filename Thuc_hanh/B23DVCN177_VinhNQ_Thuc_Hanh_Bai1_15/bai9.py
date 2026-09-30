# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Nhập vào từ bàn phím 3 số a, b, c bất kỳ.
# Kiểm tra xem 3 số a, b, c ở trên có thỏa mãn là 3 cạnh của một tam giác không.
# ❖ a, b, c có phải là 3 cạnh của tam giác cân không?
# ❖ a, b, c có phải là 3 cạnh của tam giác đều không?
# ❖ a, b, c có phải là 3 cạnh của tam giác vuông không?
# ❖ a, b, c có là 3 cạnh của tam giác vuông cân không?

# Tạo hàm riêng dùng để xét tam giác cân
def tgc(a,b,c):
    if a==b and b==c and c == a: return False   # Trả về giá trị False khi 3 cạnh bằng nhau, 3 cạnh bằng nhau là tam giác đều, không phải là tam giác cân
# Xét điều kiện khi 2 cạnh bất kì bằng nhau, nếu bằng nhau thì trả về giá trị True, nếu không thì trả về giá trị là Flase
    if a==b and a==c:
        return True
    elif b==a and b==c:
        return True
    elif c==a and c==b:
        return True        
    else: 
        return False

# Tạo hàm dùng để xét tam giác vuông
def tgv(a,b,c):
    bt = (b*b) + (c*c)                          # Tạo tham số riêng cho biểu thức để so sanh với cạnh a
    if a**a == bt:                              # Nếu tham số bt bằng a bình phương thì trả lại giá trị True, không thì trả lại giá trị False
        return True
    else:
        return False

# Tạo hàm dùng để xét tam giác vuông cân
def tgvc(a,b,c):
    ch = a*math.sqrt(2)                         # Tạo tham số dùng để so sánh với cạnh còn lại để xét trường hợp tam giác vuông cân, nếu đúng thì trả lại giá trị True và ngược lại là trả giá trị False
    if ch == c:
        return True
    else:
        return False

# Import thư viện toán
import math

# Nhập 3 lần lượt 3 cạnh tam giác
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Gọi hàm kiểm tra tam giác cân
tgc(a,b,c)
if tgc(a,b,c) == True : print("3 cạnh đã cho là tam giác cân \n")           # Nếu hàm kiểm tra tam giác cân trả lại giá trị True thì in ra màn hình 
else: print("3 cạnh đã cho không phải là tam giác cân \n")                  # Nếu hàm kiểm tra tam giác cân trả lại giá trị False thì in ra màn hình

# Kiểm tra 3 cạnh để xét tam giác đều 
if a == b == c: print("3 cạnh đã cho là tam giác đều \n")                   # Nếu 3 cạnh bằng nhau thì in ra màn hình
else: print("3 cạnh đã cho không phải là tam giác đều \n")                  # Nếu 3 cạnh hoặc 2 cạnh không bằng nhau thì in ra màn hình

# Gọi hàm kiểm tra tam giác vuông 
tgv(a,b,c)
if tgv == True: print("3 Cạnh đã cho là tam giác vuông \n")                 # Nếu hàm kiểm tra tam giác vuông trả lại giá trị True thì in ra màn hình
else: print("3 Cạnh đã cho không phải là tam giác vuông \n")                # Nếu hàm kiểm tra tam giác vuông trả lại giá trị False thì in ra màn hình

# Gọi hàm kiểm tra tam giác vuông cân
tgvc(a,b,c)
if tgvc(a,b,c) == True: print("3 cạnh đã cho là tam giác vuông cân \n")     # Nếu hàm kiểm tra tam giác vuông cân trả lại giá trị True thì in ra màn hình
else: print("3 cạnh đã cho không phải là tam giác vuông cân \n")            # Nếu hàm kiểm tra tam giác vuông cân trả lại giá trị Flase thì in ra màn hình
