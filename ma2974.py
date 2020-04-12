def tem(pala, menor):
    re = False
    for i in pala:
        if menor in i:
            re = True
        else:
            re = False
            break
    return re


pala = []
for _ in range(int(input())):
    pala.append(input())
menor = min(pala)
pala.remove(menor)
r = ['']
nr = 0
for i in range(len(menor)):
    for j in range(i, len(menor)+1):
        if tem(pala, menor[i:j:]):
            if len(r[len(r)-1]) < len(menor[i:j:]):
                r.append(menor[i:j:])

print("%s" % r[len(r)-1])
