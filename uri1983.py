def main():
    matriz = []
    for _ in range(int(input())):
        matriz.append(list(map(float, input().split())))
    maior = matriz[0][1]
    matricula = -1
    for i in range(len(matriz)):
        if matriz[i][1] >= maior and matriz[i][1] >= 8:
            matricula = int(matriz[i][0])
            maior = matriz[i][1]
    
    if matricula == -1:
        print("Minimum note not reached")
    else:
        print("%d"%matricula)


if __name__ == "__main__":
    main()