def main():
    for _ in range(int(input())):
        frase = input()
        frase_1 = frase[0:len(frase)//2:1]
        frase_2 = frase[len(frase)//2::1]
        print(frase_1[::-1]+frase_2[::-1])


main()