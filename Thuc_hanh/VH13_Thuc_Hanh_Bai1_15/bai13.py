# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Hãy nhập vào một số N với điều kiện 0<N<100.
# Yêu cầu người dùng nhập cho đến khi thỏa mãn điều kiện.

# Nhập số N từ bàn phím
n = input("Nhập số N: ")

#Dùng vòng lặp While 
while not 0 < n < 1000 : n = input("Mời bạn nhập lại số: ")             # Nếu số không thỏa mãn điều kiện thì yêu cầu người dùng nhập lại
print(n, "là số thỏa mãn điều kiện !")                                  # Nếu số thỏa mãn thì in ra màn hình