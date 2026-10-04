# Name : VinhNQ
# Date : 04/10/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Viết chương trình tính dân số của một thành phố sau 10 năm nữa, 
# biết rằng dân số hiện nay là 6.000.000, tỉ lệ tăng dân số hàng năm là 1.8%.

# Tạo biến dân số và biến tỉ lệ giống đầu bài
danso = 6000000
tl = 1.8/100
sonam = 10  

# Sử dụng công thức lũy thừa để tính dân số sau 10 năm
dan_so_sau_10_nam = danso * ((1 + tl) ** sonam )

print(f"Dân Số sau 10 năm là: {round(dan_so_sau_10_nam)}")
