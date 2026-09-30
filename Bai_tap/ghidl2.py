import os 

obj = open("dayso.txt","w", encoding="utf-8")

obj.write("\n Luu day so 1-100 \n")

for i in range (1,101):
    obj.write(f"\n đây là dòng thứ {i}")

obj.close()

obj1 = open("dayso.txt","r+", encoding="utf-8")
print(obj1.read())