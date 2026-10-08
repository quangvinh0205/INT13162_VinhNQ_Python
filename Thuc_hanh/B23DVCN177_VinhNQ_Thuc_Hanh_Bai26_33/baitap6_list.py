# Name : VinhNQ
# Date : 08/10/2026
# Mô tả yêu cầu: Cho một danh sách bất kỳ. Tính số lượng các giá trị duy nhất có trong danh sách.

# Tạo 1 danh sách bất kì chứa các phần tử ký tự và chữ số và 1 danh sách rỗng 
array = [1, "a", 34, "a", "b", 1, "c"]

# Sử dụng hàm set() để lọc các phần tử và len để tính số phần tử duy nhất có trong danh sách và in ra màn hình
soluongpt = len(set(array))
print("Số lượng phần các giá trị duy nhất có trong danh sách là:",soluongpt)
