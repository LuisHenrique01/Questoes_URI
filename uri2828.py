from math import factorial
def main():
    palavra = input()
    tam = len(palavra)
    rep = (tam - len(set(palavra))) + 1
    numerador = factorial(tam)
    denominador = cal_numerador(palavra)
    print((numerador//denominador)%((10**9) + 7))
    
def cal_numerador(palavra):
    palavra_dict = {i: j for i, j in enumerate(list(set(palavra)))}
    tam = len(palavra_dict)
    num = 1
    for i, j in enumerate(range(tam-1, tam//2, -1)):
        if j - i == 2:#impar
            num *= factorial(palavra.count(palavra_dict[i])) * factorial(palavra.count(palavra_dict[j])) * factorial(palavra.count(palavra_dict[i+1]))
        elif j - i == 3:# par
            num *= factorial(palavra.count(palavra_dict[i])) * factorial(palavra.count(palavra_dict[j])) * factorial(palavra.count(palavra_dict[i+1])) * factorial(palavra.count(palavra_dict[j-1])) 
        else:
            num *= factorial(palavra.count(palavra_dict[i])) * factorial(palavra.count(palavra_dict[j]))
    return num
        
            
if __name__ == "__main__":
    main()