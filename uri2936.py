def main():
    dic = {0: 300, 1: 1500, 2: 600, 3: 1000, 4: 150}
    gramas = [dic[i]*int(input()) for i in range(5)]
    print("%d"%(sum(gramas)+225))

main()