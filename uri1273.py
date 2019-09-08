def main():
    repet = int(input())
    while True:
        if repet == 0: break
        palavras = []
        for i in range(repet):
            palavras += [input()]
        new_palavras = retorna_indentadas(palavras)
        for j in range(len(new_palavras)):
            print(new_palavras[j])
        repet = int(input())
        if repet == 0: break
        else: print()

def retorna_indentadas(palavras):
    maior_len = int(len(palavras[retorna_maior(palavras)]))
    for i in range(len(palavras)):
        if maior_len > len(palavras[i]):
            new_palavra = palavras[i]
            for j in range(maior_len - len(palavras[i])):
                new_palavra = ' ' + new_palavra
            palavras[i] = new_palavra
    return palavras



def retorna_maior(strings):
    maior = -1
    index_maior = 0
    for i in range(len(strings)):
        if len(strings[i]) > maior:
            maior = len(strings[i])
            index_maior = i
    return index_maior


if __name__ == "__main__":
    main()