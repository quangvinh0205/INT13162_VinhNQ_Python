import os 


obj = open("test.txt","w+", encoding="utf-8")


obj.write("Phần sau của câu \n")
obj.write("hello world!!")

obj.close()