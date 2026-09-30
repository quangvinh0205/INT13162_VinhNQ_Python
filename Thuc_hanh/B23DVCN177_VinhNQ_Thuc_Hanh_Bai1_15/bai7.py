# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Nhập một tháng th bất kỳ từ bàn phím.
# ❖ Kiểm tra xem tháng th có bao nhiêu ngày.
# * Gợi ý:
# + Các tháng 1, 3, 5, 7, 8, 10 và tháng 12 có 31 ngày.
# + Các tháng 4, 6, 9 và tháng 11 có 30 ngày.
# + Đối với tháng 2 bạn cần phải nhập vào một năm n, nếu n là năm nhuận thì tháng 2
# có 29 ngày, ngược lại tháng 2 có 28 ngày (n là năm nhuận nếu nó thỏa mãn một trong 2 điều kiện: 
# điều kiện thứ nhất là n chia hết cho 4 nhưng không chia hết cho 100, 
# điều kiện thứ hai là n chia hết cho 400, ví dụ 2012 là năm nhuận, 2000 cũng là năm nhuận).

#Tạo danh sách những tháng có 30 và 31 ngày
month31 = [ 1, 3, 5, 7, 8, 10, 12]
month30 = [ 4, 6, 9, 11 ]

# Nhập số tháng 
month =input("Nhập tháng: ")

# Kiểm tra điều kiện
if month in month31:                        # Nếu tháng nằm trong danh sách 31 ngày thì in ra màn hình 
    print("Tháng", month, "có 31 ngày")
elif month in month30:                      # Nếu tháng nằm trong danh sách 30 ngày thì in ra màn hình
    print("Tháng", month, "có 30 ngày")
elif month == 2:                            # Nếu là tháng 2 thì xét những điều kiện trong khối lệnh dưới  
    year = int(input("Nhập năm: "))                             # Nhập số năm để kiểm tra
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:    # Nếu là số năm chia hết cho 4 và không chia hết cho 100 hoặc 
        print("Tháng 2 có 29 ngày")                             # chia hết cho 400 thì in ra màn hình 
    else:
        print("Tháng 2 có 28 ngày")         # Nếu không thỏa mãn điều kiện ở trên thì sẽ in ra màn hình 