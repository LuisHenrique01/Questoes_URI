def main():
    texto = input()
    if len(texto) <= 140:
        print('TWEET')
    else:
        print('MUTE')


if __name__ == "__main__":
    main()