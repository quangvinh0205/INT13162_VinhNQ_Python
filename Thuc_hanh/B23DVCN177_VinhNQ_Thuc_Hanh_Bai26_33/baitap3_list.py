# Name : VinhNQ
# Date : 07/10/2026
# Mô tả yêu cầu:Cho một danh sách gồm các số. Viết chương trình xóa các phần tử chia hết cho 2 trong danh sách.

# Tạo 1 danh sách gồm các số và 1 danh sách rỗng dùng để chứa các phần tử chia hết cho 2 
ds = [3,4,5,1,2,7,53,8,9,7,89,54]
dsr=[]

# Cho chạy vòng lặp để duyệt các phần tử trong danh sách
for i in ds:
    if i % 2 == 0:                          # Xét điểu kiện nếu chia hết cho 2 thì thêm vào cuối danh sách 
        dsr.append(i)

# In ra màn hình khi đã chạy xong vòng lặp 
print(dsr)
