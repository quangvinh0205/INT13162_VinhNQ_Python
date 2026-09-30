import os 

fo = open("test.txt", "r+", encoding="utf-8")
str = fo.read(19)
print("chuỗi đang được đọc là: ", str)

#kiểm tra vị trí
vt = fo.tell()
print("vị trí hiện tại là: ",vt)

#đặt lại vị trí
vtd = fo.seek(0,0);
str = fo.read(12)
print("đọc lại dl sau khi quay lại từ đầu: ", str)

#đóng file
fo.close()