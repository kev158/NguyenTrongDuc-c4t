map = {
    "size_x": 4,
    "size_y": 4,
}
player = {
    'x': 1,
    'y': 2
}

key = {
    "x": 2,
    "y": 1
}
exit = {
    "x": 3,
    "y": 2,
}
while True:
    for y in range(map["size_x"]):
        for x in range(map["size_y"]):
            if x == player["x"] and y == player['y']:
                print("P ", end="")
            elif x == key["x"] and y == key['y']:
                print("K", end="")
            elif x == exit["x"] and y == exit['y']:
                print("E", end="")
            else:
                print("- ", end="")

        print()
    dx = 0
    dy = 0
    move = input("Enter move W/A/S/D:")
    if move == "w":
        dy = -1
    if move == "a":
        dx = -1
    if move == "s":
       dy = 1
    if move == "d":
        dx = 1

    
    if 0 <= player['x'] + dx < map['size_x'] and 0 <= player['y'] + dy < map['size_y']:
        player['x'] += dx
        player['y'] += dy
