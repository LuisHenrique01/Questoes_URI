for _ in range(int(input())):
    n = int(input())
    a = input().split()
    p = input().split()
    prova = []
    diario = {i: {'nome': a[i], 'fre' :' '.join(p[i]).split()}for i in range(n)}
    for i in range(len(diario)):
        if ((diario[i]['fre'].count('A'))) > (((diario[i]['fre'].count('P'))+(diario[i]['fre'].count('A')))*0.25):
            prova.append(diario[i]['nome'])
    if len(prova) == 0:
        print("")
    else:
        if len(prova) == 1:
            print("%s"%prova[0])
        else:
            for i in range(len(prova)-1 ):
                print("%s"%prova[i], end=' ')
            print(prova[len(prova) - 1])