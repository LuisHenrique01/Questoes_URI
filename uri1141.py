def main():
    while True:
        strings = []
        new = int(input())
        if new == 0: break
        for _ in range(0, new):
            strings.append(input())   
        strings.sort(key=len)     
        sequencia = 0
        lista_seque = []
        for _ in range(0, 3, 1):
            index_menor = _
            for i in range(0, len(strings), 1):
                if strings[index_menor] in strings[i] or strings[i] in strings[index_menor]:
                    index_menor = i
                    sequencia += 1
            lista_seque.append(sequencia)
            sequencia = 0
        if lista_seque[0] > lista_seque[1] and lista_seque[0] > lista_seque[2]:
            print(int(lista_seque[0]))
        elif lista_seque[1] > lista_seque[0] and lista_seque[1] > lista_seque[2]:
            print(int(lista_seque[1]))
        else:
            print(int(lista_seque[2]))



"""def retorna_menor(strings):
    menor = 1001
    for i in range(len(strings)):
        if len(strings[i]) < menor:
            menor = len(strings[i])
            index_menor = i
    return index_menor"""


"""def em_ordem(strings):
    new_strings = []
    for i in range(0, len(strings)):
        index_menor = retorna_menor(strings)
        new_strings.append(strings[index_menor])
        del(strings[index_menor])
    return new_strings

"""
main()