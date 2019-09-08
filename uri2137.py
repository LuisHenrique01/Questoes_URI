def main():
    while True:
        try:
            livros = []
            for _ in range(int(input())):
                livros.append(input())
            livros.sort()
            for i in range(len(livros)):
                print(livros[i])
        except EOFError:
            break

main()