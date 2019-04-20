adv = {
    "name":"Light",
    "age":17,
    "strength":8,
    "defense":10,
    "hp":100,
    "backpack":["Shield","Bread Loaf"],
    "gold":100,
    "level":2,
}
# print(adv)
adv["gold"] += 50
adv["backpack"].append("FlintStone")
adv["pocket"]= ["MonsterDex","Flashlight"]

# print(adv)





skill1 = {
    "name":"tackle",
    "minium level":1,
    "damage":5,
    "hit rate":0.3,
}

skill2 = {
    "name":"quick attack",
    "minimum level":2,
    "damage":3,
    "hit rate":0.5,
}

skill3 = {
    "name":"strong kick",
    "minimum level":4,
    "damage":9,
    "hit rate":0.2,
}
import  random


list1 = [skill1 , skill2 , skill3]



# print(list1)
for i in range(len(list1)):
    print(i+1, list1[i]['name'])



chonskill = int(input("chon skill:"))  # print(chonskill)
for i in range(len(list1)):
    x = random.randint(0,1)
    if chonskill == 3:
        print("chua du cap do")
        break
    elif chonskill == 1 :
        print(x)
        if x < list1[0]["hit rate"]:
            print("damage",list1[0]['damage'])
        if x >       list1[0]["hit rate"]:
            print("miss")   


            break
    else :
        print(x)
        if x < list1[1]["hit rate"]:
            print("damage",list1[1]['damage'])
        if x >       list1[1]["hit rate"]:
            print("miss")   
        

        break
    


    
    






