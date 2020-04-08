from random import randint
def main():
    palavra = input()
    tam = len(palavra)
    rep = (tam - len(set(palavra))) + 1
    numerador = fatorial(tam)
    denominador = cal_numerador(palavra)
    print((numerador//denominador)%((10**9) + 7))
    
def cal_numerador(palavra):
    palavra_dict = {i: j for i, j in enumerate(list(set(palavra)))}
    tam = len(palavra_dict)
    num = 1
    for i, j in enumerate(range(tam-1, tam//2, -1)):
        if j - i == 2:#impar
            num *= fatorial(palavra.count(palavra_dict[i])) * fatorial(palavra.count(palavra_dict[j])) * fatorial(palavra.count(palavra_dict[i+1]))
        elif j - i == 3:# par
            num *= fatorial(palavra.count(palavra_dict[i])) * fatorial(palavra.count(palavra_dict[j])) * fatorial(palavra.count(palavra_dict[i+1])) * fatorial(palavra.count(palavra_dict[j-1])) 
        else:
            num *= fatorial(palavra.count(palavra_dict[i])) * fatorial(palavra.count(palavra_dict[j]))
    return num
        
        
def fatorial(tam):
    num = 1
    if tam%2 == 0:
        for i, j in enumerate(range(tam, tam//2, -1)):
            num *= (i+1) * j
    else:
        for i, j in enumerate(range(tam, tam//2, -1)):
            if i != 0:
                num *= i * j
            else:
                num *= j
    return num
            
if __name__ == "__main__":
    main()