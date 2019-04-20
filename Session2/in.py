# # # # # # # r1 = range(1,10)
# # # # # # # print(*r1)
# # # # # # # 0 1 2 3 4 5 6
# # # # # # tong = 0
# # # # # # for i in range(7):
# # # # # #     tong = tong + i
# # # # # # print(tong)

# # # # # yob = int(input("Tháng?"))

# # # # # print(yob)
# # # # # if yob < 4 :
# # # # #     print("Xuân")
# # # # # elif yob < 7 :
# # # # #     print("Hạ")
# # # # # elif yob < 10 :
# # # # #     print("Thu")
# # # # # elif yob < 13 :
# # # # #     print("Đông")
# # # # # else:
# # # # #     print("Mời bạn xem video")

# # # # import random
# # # # numb = random.randint (0,100)
# # # # print (numb)
# # # # if numb < 30:
# # # #     print("Rainy")
# # # # elif numb < 60:
# # # #     print("Cloudy")
# # # # else:
# # # #     print("Sunny")
# # # x=input("username:")
# # # y=input("password:")
# # # if x == "techkids" and y=="codethechange":
# # #     print("Welcome,superuser")
# # # elif x =="techkids":
# # #     print("Invalid password")
# # # else:
# # #     print("You are not superuser")

# # import math  
# # print("Giải phương trình bậc 2:ax^2+bx+c=0")
# # a=int(input("Nhập a:"))

# # b=int(input("Nhập b:"))
# # c=int(input("Nhập c:"))
# # delta=b**2-4*a*c

# # d = -b / 2*a
# # if delta < 0:
# #     print("PT vô nghiệm")
# # elif delta == 0:
# #     print("PT có nghiệm kép",d)
# # else:
# #     print("PT có 2 nghiệm pb")
# #     x1=(-b+ math.sqrt(delta))/2*a
# #     x2=(-b- math.sqrt(delta))/2*a
# #     print(x1)
# #     print(x2)


# x=input("username:")
# y=input("password:")
# if x == "trongduc811@gmail.com" and y == "abcxyz":
#     print("welcome,boss!")
# elif x== "trongduc811@gmail.com":
#     print("wrong password")
# else:
#     print("you are not yob
yob = int(input("Year of birth?"))
age = 2019 - yob 
print(age)
if age < 10:
    print("baby")
elif age < 20:
    print("teenager")
else:
    print("adult")

