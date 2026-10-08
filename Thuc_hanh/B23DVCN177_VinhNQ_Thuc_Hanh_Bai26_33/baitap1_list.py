# Name : VinhNQ
# Date : 07/10/2026
# Mô tả yêu cầu: Cho một danh sách bất kỳ. Viết chương trình thực hiện các yêu cầu sau:
# Xóa phần tử cuối cùng của danh sách
# Thêm một giá trị bất kỳ vào vị trí thứ 4 của danh sách
# Thay đổi giá trị của phần tử thứ nhất bằng “Python"


# Tạo 1 danh sách chứa các phần tử 
ds = ['hello','world','python']
print(ds)

# Xóa phần tử đầu tiên sử dụng pop() và in ra kết quả 
xoa=ds.pop(2)
print("phần tử bị xóa cuối cùng là:",xoa)

# Thêm 1 phần tử vào vị trí thứ 4 trong danh sách sử dụng insert() và in ra kết quả ngay sau khi xong 
ds.insert(4, 'Vinh')
print(ds)

# Thay đổi giá trị của phần tử thử nhất bằng cách chỉ mục phần tử rồi sau đấy gán giá trị
ds[0]='Python'
print(ds)