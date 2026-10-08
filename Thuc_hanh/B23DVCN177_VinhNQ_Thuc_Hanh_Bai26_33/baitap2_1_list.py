# Name : VinhNQ
# Date : 08/10/2026
# Mô tả yêu cầu: Cho một danh sách gồm các chuỗi. Viết chương trình in ra các chuỗi bắt đầu bằng chữ 'pỉ hoặc 'Р'.

# Lấy danh sách đã cho trong ví dụ, tạo thêm 1 danh sách rỗng
list_strings = ['python', 'programming', 'language', 'Python', 'most']
dsr = []
print(list_strings)

# Cho vòng lặp chạy trong list
for i in list_strings:
    if i.startswith(('pi','P','p')):                         # Xét điều kiện để kiểm tra phần tử đó có bắt đầu bằng bảng chữ 'p','P', 'pi'
       dsr.append(i)                                         # Nếu thỏa mãn thì thêm vào vị trí cuối cùng của danh sách

# In các chuỗi ra màn hình 
print("Các chuỗi bắt đầu bảng chữ 'pi', 'P', 'p' là:",dsr)