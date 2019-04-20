print("How many legs an octopus has:")
ans = {
    "1":"one leg",
    "2":"two legs",
    "3":"four legs",
    "4":"eight legs",
}
print("Where JKRowling comes from?")

ans1 = {
    "1":"England",
    "2":"America",
    "3":"ThaiLand",
    "4":"Canada ",

}
omg = 0
anss=[ans , ans1]
print(anss)
x = int(input("your answer:"))
if x == 4:
    print("hura")
    omg += 1
else:
    print("wrong")
y = int(input("ur ans:"))
if y == 1:
    print("hura")
    omg += 1
else:
    print("wrong")
print("your point:",omg)
