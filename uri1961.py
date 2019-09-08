def main():
    p, n = list(map(int, input().split()))
    lista = input().split()
    a = pula(lista, p)
    print("%s"%a)

def pula(lista, p):
    for i in range(1, len(lista), 1):
        if abs(int(lista[i])-int(lista[i-1])) > p:
            return "GAME OVER"
    return "YOU WIN"
        

if __name__ == "__main__":
    main()
