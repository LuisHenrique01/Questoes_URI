def main():
    n = int(input())
    fatias = list(map(int, input().split()))
    fatias.extend(fatias)
    dic = {e: i for e, i in enumerate(fatias)}
    dicR = {i: max([sum(list(dic.values())[k] for k in range(i, j)) for j in range(i, n+i)]) for i in range(n)}
    print("%d"%max(list(dicR.values())))


if __name__ == "__main__":
    main()