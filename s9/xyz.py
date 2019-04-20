quận = ["quận 1", "quận 2","quận 3","quận 4","quận 5","quận 6"]
dânsố = [150,247,333,266,420,318]
diệntích = [117,9,43,12,10,11]
matdodancu = 0
mậtđộ = []
for i in range(len(quận)):
    matdodancu = dânsố[i] / diệntích[i]
    mậtđộ.append(matdodancu)
    print(dânsố[i], diệntích[i])
    print(matdodancu)
    print("*" * 20)
print(mậtđộ)
