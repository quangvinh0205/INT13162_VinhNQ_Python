# Name : VinhNQ
# Date : 07/10/2026
# Mô tả yêu cầu: Cho một danh sách gồm các phần tử có giá trị bất kỳ.
# Tính tổng và trung bình cộng của các phần tử có giá trị là các số có trong danh sách.

# Tạo 1 danh sách chứa các phần tử và biến sum dùng để tính tổng các phần tử trong list
ds = [3,4,5,1,2,7,53,8,9,7,89,54]
sum = 0
print(ds)

# Tạo riêng 1 biến dùng để đếm số phần tử trong list
spt = len(ds)

# Tạo vòng lặp để cộng dồn các phần tử vào trong biến sum 
for i in ds:
    sum+=i

# Tạo biến trung bình cộng để chứa giá trị trung bình cộng sau khi tính 
tbc = sum / spt

# In kết quả tính tổng và tính trung bình cộng
print("Tổng các phần tử trong danh sách trên là:",sum)
print(f"Trung bình cộng của các phần tử có trong danh sách là: {tbc:.2f}")