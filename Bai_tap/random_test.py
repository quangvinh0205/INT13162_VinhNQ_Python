import random

a = int(input("nhap so doan random: "))
so_random = random.randint(1,100)

while a != so_random:
    if a > so_random:
        print(a,"so qua lon roi, nhap lai di")
    if a < so_random:
        print(a, "So qua nho, nhap lai")
    a = int(input("Nhap lai di tml: "))
if a == so_random :
    print("sao may rua vay ?")