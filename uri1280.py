def main():
    for _ in range(int(input())):
        pagar, receber = list(map(int, input().split()))
        if pagar == 0:
            print("%d", receber+1)