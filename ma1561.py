def main():
    while True:
        try:
            horas, minutos = tuple(map(int, input().split(':')))
            bHoras = str(bin(horas))[2::].replace('0', ' ').replace('1', 'o')
            bMinutos = str(bin(minutos))[2::].replace('0', ' ').replace('1', 'o')
            mostrar(bHoras, bMinutos)
        except EOFError:
            break
def mostrar(horas, minutos):
    if len(horas) < 4:
        n = 4 - len(horas)
        horas = ' '*n + horas
    if len(minutos) < 6:
        n = 6 - len(minutos)
        minutos = ' '*n + minutos
    print(" ____________________________________________")
    print("|                                            |")
    print("|    ____________________________________    |_")
    print("|   |                                    |   |_)")
    print("|   |   8         4         2         1  |   |")
    print("|   |                                    |   |")
    print("|   |   %s         %s         %s         %s  |   |"%(horas[0], horas[1], horas[2], horas[3]))
    print("|   |                                    |   |")
    print("|   |                                    |   |")
    print("|   |   %s     %s     %s     %s     %s     %s  |   |"%(minutos[0], minutos[1], minutos[2], minutos[3], minutos[4], minutos[5]))
    print("|   |                                    |   |")
    print("|   |   32    16    8     4     2     1  |   |_")
    print("|   |____________________________________|   |_)")
    print("|                                            |")
    print("|____________________________________________|")
    print('')


    
    
if __name__ == "__main__":
    main()