# Name : VinhNQ
# Date : 07/10/2026
# Mô tả yêu cầu: Cho một danh sách bất kỳ. Viết chương trình hoán đổi phần tử đầu tiên và vị trí cuối cùng của danh sách.

# Tạo 1 danh sách riêng
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Sử dụng kĩ thuật hoán đổi đồng thời (a,b = b,a)
motorcycles[0], motorcycles[2] = motorcycles[2], motorcycles[0]
print(motorcycles)
