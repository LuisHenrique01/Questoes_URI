men = input()
crib = input()
cont=0
for i in range(len(men)):
    igual = False
    men2 = men[i:len(crib)+i:]
    if len(men2)<len(crib):break
    for j in range(len(crib)):
        if men2[j] == crib[j]:
            igual= True
            break
    if not igual:
        cont+=1
print("%d"%cont)
