def main():
    entrega, data_limite = list(map(int, input().split()))
    if data_limite - entrega < 0: print('Eu odeio a professora!')
    elif data_limite - entrega >= 3: print('Muito bem! Apresenta antes do Natal!')
    else:
        print('Parece o trabalho do meu filho!')
        if entrega + 2 < 24: print('TCC Apresentado!') 
        else: print('Fail! Entao eh nataaaaal!')


main()