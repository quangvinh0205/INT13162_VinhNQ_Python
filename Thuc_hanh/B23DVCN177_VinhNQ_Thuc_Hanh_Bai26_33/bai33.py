# Name : VinhNQ
# Date : 04/10/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Viết chương trình giải bài toán cổ điển sau:
# ❖ Trăm trâu, trăm cỏ
# ❖ Trâu đứng ăn năm
# ❖ Trâu nằm ăn ba,
# ❖ Ba trâu già ăn một
# ❖ Hỏi mỗi loại trâu có bao nhiêu con.

# Tạo 1 hàm riêng để giải bài toán
def gbttt (duoc_phep_bang_khong: bool = False):                 # Tham số duoc_phep_bang_khong có giá trị mặc định là False
    # Thực hiện toán tử 3 ngôi và gán giá trị cho biến đếm trâu
    gtbd = 0 if duoc_phep_bang_khong else 1     
    # Tạo 1 biến đếm dùng để đếm kết quả                
    count = 0
    print(f"Kết quả với điều kiện số trâu mỗi loại >= {gtbd}")
    print(f"{'Các đáp án':<12} | {'Trâu đứng':<12} | {'Trâu nằm':<12} | {'Trâu già':<12}")              # {'Các đáp án':<12} là căn lề rộng 12 ký tự và căn lề sang bên trái (String formatting) 

# Tạo vòng lặp để tìm từng con trâu, với i là con trâu đứng, j là con trâu nằm, g là con trâu già
# Vì trâu đứng không thể quá 20 con và trâu nằm không thể quá 33 con 
    for i in range (gtbd, 21):                                              # Duyệt số lượng trâu đứng
        for j in range (gtbd, 34):                                          # Duyệt số lượng trâu nằm
            # Biểu thức tính trâu già 
            g = 100 - i -j
            # Kiểm tra điều kiện của trâu già: số trâu già phải không âm, số trâu già phải chia hết cho 3 và tổng số bó cỏ phải ăn hết đúng 100 bó cỏ 
            if g >= gtbd and (g % 3 == 0 ) and (5 * i + 3 * j + g // 3 == 100):
                count +=1                                                                               # Tăng biến đếm lên 1
                print(f"Đáp án {count:<4}  | {i:<13}| {j:<13}| {g:<13} ")                             # {'Đáp án':<13} là căn lề rộng 12 ký tự và căn lề sang bên trái (String formatting)
    # Xét điều kiện nếu biến đếm bằng 0 thì không có kết quả 
    if count == 0:                              
        print("Không tìm thấy đáp án !")
    # Nếu trong bài có bao nhiêu đáp án thì in ra màn hình
    else:
        print(f"Có {count} đáp án thỏa mãn")
        print()


# Gọi hàm giải bài toán với tham số có 2 giá trị là True và False
gbttt(duoc_phep_bang_khong=False)
gbttt(duoc_phep_bang_khong=True)

