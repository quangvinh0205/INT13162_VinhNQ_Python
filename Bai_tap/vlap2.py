num= int(input("Nhập số: "))

# while num < 120:
#     print(num)
#     num += 5

while not (0 < num < 120):
    num = int(input("Nhập lại số: "))
print("Số hợp lệ: ", num)