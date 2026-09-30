# Name : VinhNQ
# Date : 14/09/2026
# Mô tả yêu cầu: 
# Sử dụng ngôn ngữ lập trình Python. 
# Hãy nhập vào tuổi của một người và đưa ra kết luận và lứa tuổi của người đó theo quy tắc sau:
# ❖ Tuổi > 0 và <=2 là trẻ sơ sinh
# ❖ Tuổi >2 và <=10 là nhi đồng
# ❖ Tuổi >10 và <=17 là vị thành niên
# ❖ Tuổi > 17 và <=39 là thanh niên
# ❖ Tuổi >39 và <=50 là trung niên
# ❖ Tu tuổi >50 là cao niên.

# Nhập số tuổi từ bàn phím
age=int(input())

# Xét điều kiện
if (age > 0 and age <= 2):          # Nếu độ tuổi lớn hơn 0 và tuổi dưới hoặc bằng 2 thì in ra màn hình 
    print("trẻ sơ sinh")
elif (age > 2 and age <= 10):       # Nếu độ tuổi lớn hơn 2 và tuổi dưới hoặc bằng 10 thì in ra màn hình 
    print("nhi đồng")
elif (age > 10 and age <= 17):      # Nếu độ tuổi lớn hơn 10 và tuổi dưới hoặc bằng 17 thì in ra màn hình 
    print("vị thành niên")
elif (age > 17 and age <= 39):      # Nếu độ tuổi lớn hơn 17 và tuổi dưới hoặc bằng 39 thì in ra màn hình 
    print("thanh niên")
elif (age > 39 and age <= 50):      # Nếu độ tuổi lớn hơn 39 và tuổi dưới hoặc bằng 50 thì in ra màn hình 
    print("trung niên")
else:                               # Nếu độ tuổi lớn hơn 50 thì in ra màn hình 
    print("Cao niên")