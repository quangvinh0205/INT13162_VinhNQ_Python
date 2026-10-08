# Name : VinhNQ
# Date : 07/10/2026
# Mô tả yêu cầu: Cho một danh sách số. Viết chương trình in ra các số có số lần xuất hiện lớn hơn hoặc bằng 3 (lần).

# Import thư viện Collection 
import collections

# Danh sách số cho sẵn và tạo 1 danh sách rỗng
list_numbers = [1, 5, 1, 8, 4, 1, 4, 3, 2, 8, 4, 9]
ds = []
print(list_numbers)

# Tạo biến dem dùng để đếm tần suất xuất hiện các phần tử 
dem = collections.Counter(list_numbers) 

# Chạy vòng lặp để lọc các phần tử xuất hiện trên hoặc 3 lần trong danh sách
for i, c in dem.items():
    if c >= 3:
        ds.append(i)

# In ra màn hình các phần tử xuất hiện 3 lần hoặc hơn trong danh sách
print(ds)