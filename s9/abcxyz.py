highscore = [45,67,56,78,1,2,3,4]
# # it = ["a", "b", "c"]
# # for i,items in enumerate(it):
# #     print(i+1,".",items)
while True:
    for i , items in enumerate(highscore):
        if i <= 4:
            print(i+1,".",items)
    s = int(input("new highscore: "))
    highscore.append(s)
    print(highscore)
    highscore.sort()
    highscore.reverse()
    print(highscore)