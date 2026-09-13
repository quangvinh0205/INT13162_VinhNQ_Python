# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. 
# Hãy nhập vào 1 điểm trung bình và xét học bổng đối với điểm trung bình đó theo quy tắc sau:
# ❖ Nếu điểm trung bình > =9 thì học bổng là 5000000
# ❖ Nếu điểm trung bình >=8 và <9 thì học bổng là 3000000
# ❖ Nếu điểm trung bình >=7 và <8 thì học bổng là 1000000
# ❖ Những trường hợp còn lại học bổng = 0.

# Nhập số điểm từ bàn phím
grade = int(input("Nhập điểm tb: "))

# Xét điều kiện 
if(grade >= 9):                             # Nếu điểm trên hoặc bằng 9 thì in ra màn hình
    print("Học Bổng: 5.000.000")
elif(grade >= 8):                           # Nếu điểm trên hoặc bằng 8 và dưới 9 thì in ra màn hình 
    print("Học Bổng: 3.000.000")
elif(grade >= 7):                           # Nếu điểm trên hoặc bằng  7 và dưới 8 thì in ra màn hình 
    print("Học Bổng: 1.000.000")
else:                                       # Nếu điểm dưới 7 thì in ra màn hình 
    print("Học Bổng : 0")                   