maytinh = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30,
}





x = maytinh[input("LAPTOP?")]
print("số lượng máy",":",x)






maytinh["TOSHIBA"] = 10
maytinh[input("TYPE?")] = int(input("number?"))
print(maytinh)
maytinh["DELL"]   += 10
maytinh["MACBOOK"]   -= 2
print(maytinh)

tongsomay = sum(maytinh.values())
print("tổng số máy",":",tongsomay)




maytinh["FUJITSU"] = 15
maytinh["ALIENWARE"] = 5




giamaytinh = {
    "HP":600,
    "DELL":650,
    "MACBOOK":12000,
    "ASUS":400,
    "ACER":350,
    "TOSHIBA":600,
    "FUJITSU":900,
    "ALIENWARE":1000,
}
gia = giamaytinh[input("kinda laptop:")]
print("giá",":",gia)

giamuaasus = giamaytinh["ASUS"]*5
print("giá máy asus",":",giamuaasus)


print(maytinh)



print("Nhập loại máy tính và số lượng máy xuất kho?")
abc = sum(maytinh.values())
maytinh[input("type?")]=int(input("nummber?"))
xyz = sum(maytinh.values())

maytinhxuatkho =  abc - xyz
print("số loại máy vừa nhập sau khi xuất kho",",",maytinhxuatkho)
print("số máy còn lại trog kho",":",xyz)
print(maytinh)




list1 =[]
list1.append(maytinh)
list1.append(giamaytinh)
print(list1)

for key in maytinh.keys():
    if key in giamaytinh.keys():
        print(maytinh[key]*giamaytinh[key])
        