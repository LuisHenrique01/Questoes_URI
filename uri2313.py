def main():
    valores = input()
    a = int(my_split(valores, ' ')[0])
    b = int(my_split(valores, ' ')[1])
    c = int(my_split(valores, ' ')[2])

    if eh_triagulo(a, b, c):
        print('Valido-%s'%qual_tipo(a, b, c))
        if eh_retangulo(a, b, c):
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    else:
        print('Invalido')


def qual_tipo(a, b, c):
    if a == b and b == c:
        return 'Equilatero'
    elif a == b or a == c or b == c:
        return 'Isoceles'
    else:
        return 'Escaleno'


def eh_retangulo(a, b, c):
    if a > b and a > c:
        return a == ((b**2) + (c**2))**0.5
    elif b > a and b > c:
        return b == ((a**2) + (c**2))**0.5
    else: 
        return c == ((a**2) + (b**2))**0.5


def eh_triagulo(a, b, c):
    return (abs(b-c) < a and a < b + c) and (abs(a-c) < b and b < a + c) and (abs(b-a) < c and c < b + a) 


def my_split(valores, splitador):
    vetor = []
    valor = ''
    for i in range(len(valores)):
        if valores[i] != splitador:
            valor += valores[i]
            if len(valores) - 1 == i:
                vetor += [valor]
        else:
            vetor += [valor]
            valor = ''
    return vetor


if __name__ == "__main__":
    main()