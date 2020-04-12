for _ in range(int(input())):
    input()
    alunos = list(map(int, input().split()))
    alunosC = sorted(alunos)[::-1]
    trocas = 0
    for i in range(len(alunos)):
        if alunos[i] == alunosC[i]:
            trocas += 1
    print("%d"%trocas)