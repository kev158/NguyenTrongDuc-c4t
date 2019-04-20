from random import randint, choice
count = 0

while True:
    a = randint(0,10)
    b = randint(0,10)
    op = choice(["+", "-", "*", "/"])
    res = 0
    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    else:
        res = a / b

    err = randint(-1,1)
    display_res = res + err
    print(a, op, b, "=",display_res)
    asw = input("Ban chon dung hay sai?")
    if err == 0 :
        if asw == "dung":
            count += 1
        else:
            break
    
    elif err != 0:
        if err == -1:
            if asw == "sai":
                count += 1
            else:
                break
        elif err == 1:
            if asw == "sai":
                count += 1
            else:
                break
    print(count)
            


    