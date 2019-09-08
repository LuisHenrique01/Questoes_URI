def main():
    n = int(input())
    pecas = list(map(int, input().split()))
    compa = [i for i in range(1, n+1, 1)]
    fatando = [compa[i] for i in range(len(compa)) if not compa[i] in pecas]
    for i in range(len(fatando)): print("%d"%fatando[i])

main()