# Name : VinhNQ
# Date : 07/10/2026
# Mô tả yêu cầu: Cho một danh sách gồm các số. Tính bình phương các phần tử trong danh sách và sắp xếp theo thứ tự giảm dần..

# Tạo 1 danh sách chứa các phần tử và 1 danh sách rỗng dùng để chứa các phần tử sau khi đã tính bình phương
ds = [3,4,5,1,2,7,53,8,9,7,89,54]
dsr = []
print(ds)

# Tạo 1 vòng lặp chạy trong danh sách để tính bình phương các phần tử
for i in ds:
    bp = i**2
    dsr.append(bp)              # Sau khi đã tính bình phương thì đưa kết quả vào vị trí cuối cùng trong danh sách
# Sau khi tính xong thì in ra màn hình
print("Danh sách bình phương các phần tử trong danh sách:",dsr)

# Khi đã có danh sách tính bình phương các phần tử trong danh sách thì sử dụng sort(reverse=True) để đảo ngược danh sách theo thứ tự alphabet() và in ra màn hình
dsr.sort(reverse=True)
print("Danh sách sau khi đã đảo ngược:",dsr)