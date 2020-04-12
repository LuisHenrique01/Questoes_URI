def main():
    while True:
        n = int(input())
        if n == 0: break
        lista = []
        for i in range(n):
            lista.append(input())
        ruim = False
        for i in range(n):
            for j in range(n):
                if i != j and lista[i] in lista[j]:
                    ruim = True
                    break
        if ruim:
            print("Conjunto Ruim")
        else:
            print("Conjunto Bom")
                

main()