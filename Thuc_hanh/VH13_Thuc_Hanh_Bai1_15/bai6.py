# Name : VinhNQ
# Date : 13/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Nhập một ký tự ch bất kỳ từ bàn phím.
# ❖ Kiểm tra xem ký tự ch là nguyên âm, phụ âm, ký số (ký tự số) hay ký tự khác.


# Nhập từ bàn phím 
# Hàm strip() sẽ bỏ qua khoảng trắng thừa
# Hàm lower() sẽ đồng nhất tất cả mọi ký tự
kt = input("Nhập một ký tự bất kì: ").strip().lower()

# Tạo danh sách chứa các nguyên âm, phụ âm, phụ âm kép, ký số sang dạng chuỗi (string)
nguyenam = ["a", "ă", "â", "e", "ê", "i", "o", "ô", "ơ", "u", "ư", "y"]
phuam = ["b", "c", "d", "đ", "g", "h", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x"]
phuamkep = ["ch", "gh", "gi", "kh", "ng", "ngh", "nh", "ph", "qu", "th", "tr"]
kyso = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Xét điều kiện
if kt in nguyenam : print(kt, "là nguyên âm ")          # Nếu ký tự thuộc trong danh sách nguyên âm thì in ra màn hình
elif kt in phuam : print(kt,"là phụ âm")                # Nếu ký tự thuộc trong danh sách phụ âm thì in ra màn hình
elif kt in phuamkep : print(kt,"là phụ âm kép")         # Nếu ký tự thuộc trong danh sách phụ âm kép thì in ra màn hình
elif kt in kyso : print(kt,"là ký số")                  # Nếu ký tự thuộc trong danh sách ký số thì in ra màn hình
else : print(kt, "là ký tự khác")                       # Nếu ký tự không thuộc trong danh sách thì in ra màn hình