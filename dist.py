m, n, k = list(map(int, input().split()))
vet = [list(map(int, input().split())) for i in range(k)]
#vet.insert(0, [0, 0, 0])
#vet.append([m, n, 0])
for i in range(3):
    if abs((((vet[i][0]-vet[i+1][0])**2) + ((vet[i][1]-vet[i+1][1])**2))**0.5) > vet[i][2]+vet[i+1][2]:
        rouba = True
    else:
        rouba = False
        break
if rouba:
    print("S")
else:
    print("N")