while True:
    n, m = tuple(map(int, input().split()))
    if n == m and m == 0: break
    foto = [input() for i in range(n)]
    a, b = tuple(map(int, input().split()))
    repN = a//n
    repM = b//m
    new_foto = [''.join([j*repM for j in list(i)]) for i in foto]
    foto_final = []
    for j in new_foto:
        for i in range(repN):
            foto_final.append(j)
        
    for i in foto_final:
        print("%s"%i)
    print('')