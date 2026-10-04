# Name : VinhNQ
# Date : 04/10/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Viết chương trình tìm USCLN, BSCNN của 2 số nguyên dương

# Import thư viện toán
import math

# Nhập 2 số a,b từ bàn phím
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
while a < 0 and b < 0:
    a = int(input("Nhập lại số a: "))
    b = int(input("Nhập lại số b: "))

uscln = math.gcd(a,b)                   # Hàm math.gcd() dùng để tìm ước số chung lớn nhất của các số
bscnn = math.lcm(a,b)                   # Hàm math.lcn() dùng để tìm bội số chung nhỏ nhất của các số

# In ra màn hình 2 kết quả
print(f"Ước số chung lớn nhất của {a} và {b} là {uscln}")
print(f"Bội số chung nhỏ nhất của {a} và {b} là {bscnn}")