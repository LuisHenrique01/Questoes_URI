def main():
    vet = list(map(int, input().split()))
    icm = vet[0]/(vet[1]+vet[2])
    print("%.2f"%icm)

main()