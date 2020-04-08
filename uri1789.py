import random
def main():
    while True:
        try:
            input()
            lista = list(map(int, input().split()))
            lista.sort()
            if lista[len(lista) - 1] < 10:
                print("1")
            elif lista[len(lista) - 1] < 20:
                print("2")
            else:
                print("3")
        except EOFError:
            break

            
if __name__ == "__main__":
    main()
