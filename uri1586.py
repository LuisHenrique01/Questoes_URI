def main():
    while True:
        num_estu = int(input())
        if num_estu == 0: break
        alunos = [input() for i in range(num_estu)]
        scor = [sum([ord(l) for l in list(aluno)]) for aluno in alunos]
        aluno = ''
        for i in range(len(scor)):
            a = scor[:i+1:]
            b = scor[i+1::]
            a = [(a[i]*(i+1)) for i in range(len(a))]
            b = [(b[i]*(i+1)) for i in range(len(b))]
            if sum(a) == sum(b):
                aluno = alunos[i]
        if aluno == '':
            print('Impossibilidade de empate.')
        else:
            print('%s'%aluno)
            
            
main()