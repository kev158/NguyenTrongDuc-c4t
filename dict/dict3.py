person = {
    "name":"duc",
    "age":15,
}
y = input("nhập key:")

x= y in person
if y == "name":
    print("exist")
elif y == "nationality":
    print("no exit")

print(person)
print(x)
