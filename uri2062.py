def main():
    num_palavras = int(input())
    palavras = input().split()
    dici = {i: palavras[i] for i in range(len(palavras))}
    for i in range(len(dici)):
        if len(dici[i]) == 3 and 'OB' in dici[i]:
            dici[i] = 'OBI'
        elif len(dici[i]) == 3 and 'UR' in dici[i]:
            dici[i] = 'URI'
    for i in range(len(dici)-1):
        print("%s"%dici[i], end = ' ')
    print(dici[len(dici)-1])


if __name__ == "__main__":
    main()