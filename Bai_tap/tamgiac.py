num1 = int(input("Nhập số: "))

for i in range (1,num1 + 1):
    str=" "
    for j in range (1,i + 1):
        str+="*"
    print(str)