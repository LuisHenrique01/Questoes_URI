import random
numero = int(input(), 2)
dic = {i: int(input()) for i in range(int(input()))}
vet = []
for i in range(len(dic)):
    if numero%dic[i] == 0:
        vet.append(dic[i])
vet.sort()
if len(vet) == 0:
    print("Nenhum")
else:
    for i in range(len(vet)-1):
        print("%d"%vet[i], end=' ')
    print("%d"%vet[len(vet)-1])