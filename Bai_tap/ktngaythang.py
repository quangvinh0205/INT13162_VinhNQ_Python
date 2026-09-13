month31 = [ 1, 3, 5, 7, 8, 10, 12]
month30 = [ 4, 6, 9, 11 ]

month = int(input("Nhập tháng: "))
if month in month31:
    print("Tháng", month, "có 31 ngày")
elif month in month30:
    print("Tháng", month, "có 30 ngày")
elif month == 2:
    year = int(input("Nhập năm: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: 
        print("Tháng 2 có 29 ngày")
    else:
        print("Tháng 2 có 28 ngày")
else:
    print("Tháng gì đây ? Nhập lại đi !")