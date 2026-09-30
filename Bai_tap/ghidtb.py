import os

obj = open("diemtb.txt", "a", encoding="utf-8")

#viết thông báo
name= input('Nhập họ tên của bạn: ')
scoretb = float(input("nhập điểm tb"))
obj.write(f"\n {name}")