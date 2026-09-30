import os 

file_open = open("test.txt","a")
print("Tên file: ",file_open.name)
print("Kiểm tra trạng thái của file: ",file_open.closed)
print("Mode open file: ",file_open.mode)