def main():
    num = int(input())
    primos = [i for i in range(num//3) if primo(i)]
    print(primos)

def primo(numero):   
    div = 0
    parada = int(numero**0.5) + 1
    for i in range(1, parada, 1):
        if numero % i == 0:
            div += 1
            if div > 1:
                break
    if numero == 1 or div > 1:
        return False
    else:
        return True
    
    
if __name__ == "__main__":
    main()