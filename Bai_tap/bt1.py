age=int(input())
if (age > 0 and age <= 2): 
    print("trẻ sơ sinh")
elif (age > 2 and age <= 10):
    print("nhi đồng")
elif (age > 10 and age <= 17):
    print("vị thành niên")
elif (age > 17 and age <= 39):
    print("thanh niên")
elif (age > 39 and age <= 50):
    print("trung niên")
else:
    print("Cao niên")