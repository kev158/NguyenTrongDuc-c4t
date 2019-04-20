book={
    "name":"Harry Potter",
    "year":1976,
    "characters":["Harry","Ron","Luna"]
}
book["nation"]="england"
for k , v in book.items():
    print(k,"-" , v)
book["characters"]=["Hermione","Ronnie","Jack"]
book["characters"].append("snape")
book["characters"].pop(0)
print(book)
print(book["characters"][1])
