from itertools import product
n = int(input())
pred = list(map(int, input().split()))
 
permsList = [''.join([j for j in product(pred, repeat=i)]) for i in range(1, n)]
print(set(permsList))