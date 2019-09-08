def main():
    for _ in range(0, int(input())):
        texto = input()
        primeira = primeira_passada(texto)
        segunda = segunda_passada(primeira)
        terceira = terceira_passada(segunda)
        print(terceira)


def primeira_passada(texto):
    novo_texto = ''
    for i in range(len(texto)):
        if e_letra(texto[i]):
            novo_texto = novo_texto + chr(ord(texto[i]) + 3)
        else:
            novo_texto = novo_texto + texto[i]
    return novo_texto


def segunda_passada(texto):
	return texto[::-1]


def terceira_passada(texto):
    apartir_meio = ''
    antes_meio = ''
    for i in range((len(texto)//2), len(texto)):
            apartir_meio = apartir_meio + chr(ord(texto[i]) - 1)
    
    for j in range(0, len(texto)):
        if len(texto) // 2 > j:
            antes_meio = antes_meio + texto[j]
 
    return antes_meio + apartir_meio


def e_letra(caracter):
    return (ord(caracter) > 64 and ord(caracter) < 91) or (ord(caracter) > 96 and ord(caracter) < 123)


if __name__ == "__main__":
    main()