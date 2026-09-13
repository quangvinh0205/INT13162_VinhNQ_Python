# Name : VinhNQ
# Date : 13/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Nhập 4 số từ bàn phím a, b, c, d. 
# Ví dụ: Nhập 4 số a=3, b=5, c=2, d=4.
# ❖ Hãy tìm và in ra giá trị lớn nhất (Max) và nhỏ nhất (Min) trong các số trên.
# ❖ Hãy in ra các số theo thứ tự tăng dần (2 3 4 5) và thứ tự giảm dần (5 4 3 2).

# Nhập vào từ bàn phím 4 số a, b, c, d 
# Nhập 4 phần tử a, b, c, d
# [Hàm map(function, iterable) dùng để áp dụng cho 1 hàm trong danh sách.]
# [Hàm split(separator, maxsplit) dùng để tách một chuỗi thành một danh sách con dựa trên 1 ký tự hoặc chuỗi đã cho ]
a = list(map(int, input("Nhập lần lượt 4 số a, b, c, d: ").split()))                 

# Sắp xếp mảng có 4 phần tử từ nhỏ tới lớn (Hàm sort() dùng để sắp xếp các phần tử trong danh sách)
a.sort()

# Đảo danh sách a đã sắp xếp ở trên
# (Hàm sorted() dùng để sắp xếp các phần tử của một đối tượng có thể lặp lại) 
# (Hàm reverse=True dùng để đảo ngược lại toàn bộ phần tử ngay trong danh sách)
sapxepltn=sorted(a, reverse=True)

# In ra kết quả 
print("Số lớn nhất là:", sapxepltn[0])                      # Số Lớn Nhất
print("Số nhỏ nhất là:", a[0])                              # Số Nhỏ nhất
print("4 số đã được sắp xếp từ nhỏ tới lớn là:",a)          # Sắp xếp từ nhỏ tới lớn
print("4 số đã được sắp xếp từ lớn tới nhỏ là:",sapxepltn)  # Sắp xếp từ lớn tới nhỏ