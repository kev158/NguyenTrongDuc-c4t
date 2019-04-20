# english = {
#     "man":"đàn ông",
#     "woman":"đàn bà",
# }
# print(english)


pikachu= {
    "raichu":"electric",
    "onix":"giant",
}
print(pikachu)
while True:

    pikachu["raichu"] = "It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will evolve into this form regardless of their origin."
    pikachu["onix"] = " It has a rocky spine on its head and a pair of black eyes right beneath it. This Pokémon has a magnet in its brain that serves as an internal compass. Its body absorbs many hard objects, making its body very solid. As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds."
    x = input("pikachu name:")
    if x == "raichu":
        print(pikachu["raichu"])
    elif x == "onix":
        print(pikachu["onix"])
    else:
        break