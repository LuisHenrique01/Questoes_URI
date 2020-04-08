def main():
    n = int(input())
    i = 1
    while i <= n:
        lista = list(map(float, input().split()))
        anos = 0
        while lista[0] <= lista[1]:
            lista[0] += int(lista[0] * (lista[2]/100))
            lista[1] += int(lista[1] * (lista[3]/100))
            anos += 1
            if anos > 100:
                break
        if anos > 100:
            print('Mais de 1 seculo.')
        else:
            print('%i anos.'%anos) 
        i += 1
    

if __name__ == "__main__":
    main()