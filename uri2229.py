testes = 1
while True:
    n = int(input())
    if n == -1: break
    dobras = (1 + (n*2)) * (1 + (n*2)) 
    print("Teste %d"%testes)
    if n == 0:
        print('4')
    else:
        print("%d"%dobras)
    print("")
    testes += 1