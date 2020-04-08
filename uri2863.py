def main():
    while True:
        try:
            vetor = [float(input()) for _ in range(int(input()))]
            print(min(vetor))
        except EOFError:
            break
    

main()