def main():
    valor = int(input())
    teste = 1
    while valor != 0:
        cedula50 = 0
        cedula10 = 0
        cedula5 = 0
        cedula1 = 0
        if valor >= 50:
            cedula50 += valor // 50
            valor = valor % 50
        if valor >= 10:
            cedula10 += valor // 10
            valor = valor % 10
        if valor >= 5:
            cedula5 += valor // 5
            valor = valor % 5
        if valor >= 1:
            cedula1 += valor // 1
            valor = valor % 1
        print('Teste %s'%teste)
        print("%d %d %d %d"%(cedula50, cedula10, cedula5, cedula1))
        valor = int(input())
        print("")
        teste += 1


main()
