# # # # item = ["a","b","c"]
# # # # print(item)
# # # # d=input("Nhao vao:")
# # # # item.append(d)

# # # # print(item)

# # # item = [ "a","b","c" ]
# # # print(item)
# # # d = input ("Nhap vao:")
# # # item.append(d)
# # # print(item)
# # # q= int(input("Nhap so:"))

# # # print(*item[0].upper())
# # # print(*item[3].upper())
# # # print(*item[q].upper())


# # items = ["sport", "lol ","bts"]
# # d = input("one more?")
# # items.append(d)
# # print(*items,sep="|")
# # items[1] = input("whatever?")
# # print(items)
# # items.remove('sport')
# # print(items)

# # it = ["a", "b", "c"]
# # for i,items in enumerate(it):
# #     print(i+1,".",items)

# # d = input("nhap linh tinh: ")
# # it.append(d)
# # print(it)
# # e =input("nhap linh tinh:")

# # items.append(e)

# new_list = ["DEATHNOTE", "NETFLIX", "a", "b"]
# for i in new_list:
#     if "E" in i or "e" in i:
#         print(i)

list1 = ["lol", "fornite", "dota2"]
while True:
        m = input("choose one: C,R,U,D")



        if m == "C" :
                d = input("game yeu thich?")
                list1.append(d)
                print(*list1,sep=",")
        elif m == "R":
                for i in list1:
                        print(i)
        elif m == "U":
                posi = int(input("Enter posi: "))
                value = input("Enter value: ")
                list1[posi] = value
                print(list1)
        elif m == "D":
                posi1 = int(input("Enter posi:  "))
                list1.pop(posi1)
                print(list1)
        else:
                print("wrong!")






