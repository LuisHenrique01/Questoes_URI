def main():
    for _ in range(int(input())):
        medias = list(map(int, input().split()))
        soma = 0
        for i in range(1, len(medias)): soma += medias[i]
        media_turma = soma/medias[0]
        alunos_acima = 0
        for i in range(1, len(medias)): 
            if medias[i] > media_turma:
                alunos_acima += 1
        percente = (alunos_acima*100)/(len(medias) - 1)
        print("%.3f%%"%percente)


if __name__ == "__main__":
    main()