qtd = int(input())
valor = 7
for i in range(11, qtd+1):
    if i < 31:
        valor += 1
    elif i < 101:
        valor += 2
    else:
        valor += 5
print("%d"%valor) 