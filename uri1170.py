def mian():
    for _ in range(int(input())):
        sup = float(input())
        cont = 0
        while sup > 1:
            cont += 1
            sup = sup / 2
        print("%d dias"%cont)


mian()