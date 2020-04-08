def main():
    for _ in range(0, int(input())):
        leds = 0
        numero = input()
        for i in range(0, len(numero)):
            leds += valor_leds(numero[i])
        print('%i leds'%leds)


def valor_leds(num):
    if num == '1':
        return 2
    elif num == '2':
        return 5
    elif num == '3':
        return 5
    elif num == '4':
        return 4
    elif num == '5':
        return 5
    elif num == '6':
        return 6
    elif num == '7':
        return 3
    elif num == '8':
        return 7
    elif num == '9':
        return 6
    else:
        return 6


main()