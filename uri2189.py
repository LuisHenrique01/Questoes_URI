testes = 1
while True:
    n = int(input())
    if n == 0: break
    entrada = list(map(int, input().split()))
    print('Teste %d'%testes)
    for i, j in enumerate(entrada):
        if i+1 == j:
            print("%d"%j)
    print('')
    testes += 1