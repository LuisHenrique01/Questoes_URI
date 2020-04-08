def main():
    while True:
        l = list(input().split())
        w1 = int(l[0])
        w2 = int(l[1])
        r = int(l[2])
        if w1 == 0 and w2 == 0 and r == 0: break
        bd = w1*(1+(r/30))
        be = w2*(1+(r/30))
        media = (bd + be)/2
        if media < 13:
            print('Nao vai da nao')
        elif media < 14:
            print('E 13')
        elif media < 40:
            print('Bora, hora do show! BIIR!')
        elif media <= 60:
            print('Ta saindo da jaula o monstro!')
        else:
            print('AQUI E BODYBUILDER!!')
    print()
    print('Aqui nois constroi fibra rapaz! Nao e agua com musculo!')

if __name__ == "__main__":
    main()