# Name : VinhNQ
# Date : 08/10/2026
# Mô tả yêu cầu: Cho một danh sách số. Viết chương trình tính tổng tích lũy của một danh sách, 
# nghĩa là, kết quả là một danh sách mới trong đó phần tử thứ i là tổng của i+1 phần tử đầu tiên từ danh sách ban đầu.

# Tạo 1 danh sách số, 1 danh sách rỗng và biến tổng bằng 0
dss = [64,73,4,2,46,53,54,7,87,90,42,22,97,88]
dsr = []
tong = 0
print("Danh sách cũ:",dss)

# Chạy vòng lặp trong danh sách để duyệt từng phần tử
for i in dss:
    tong += i                       # Cộng dồn phần tử hiện tại vào biến tổng
    dsr.append(tong)                # Thêm giá trị đã tính tổng hiện tại vào cuối danh sách

# In ra kết quả ra màn hình
print("Danh sách tính tổng tích lũy của 1 danh sách là:",dsr)