# Name : VinhNQ
# Date : 29/09/2026
# Mô tả yêu cầu: Sử dụng ngôn ngữ lập trình Python. Bạn hãy viết chương trình in ra 10 số đầu tiên của dãy số Fibonacci. 

# Tạo hàm riêng cho dãy số fibonacci
def fibonacci(n):
    a,b = 0,1                                   # Khởi tạo 2 số đầu tiên của dãy Fibonacci là 0 và 1 
    count = 0                                   # Tạo biến đếm bằng 0
    if n == 1:                                  # Xét trường hợp n bằng 1 thì sẽ in ra số a
        print(a)                                
    else:                                       # Nếu n lớn hơn 1 thì sẽ chạy vòng lặp while 
        print("Dãy fibonacci là: ")
        while count < n:                        # Vòng lặp chạy từ 0 cho tới số n 
            print(a,end=" ")                    
            a,b = b , a + b                     # Cập nhật giá trị mới cho a (là số tiếp theo) và b (là tổng của 2 số trước đó)
            count += 1                          # Biến đếm tăng lên 1 

fibonacci(10)                                   # Gọi hàm fibonacci(10) chứa tham số là 10 
