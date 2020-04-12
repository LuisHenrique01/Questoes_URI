tam = int(input())
fatias = list(map(int, input().split()))
fatias.extend(fatias)
resp = max(0, fatias[0])
for i in range(1, 2*tam-1):
    fatias[i] = max(fatias[i], fatias[i] + fatias[i-1])
    resp = max(resp, fatias[i])  
print("%d"%resp)  