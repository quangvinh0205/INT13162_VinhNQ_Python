num = int(input("Nhap so bat ki: "))

for i in range(1, num + 1, 1): #(start, stop, step)
    if (num % i == 0):
        print(i, end = " ")