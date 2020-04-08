def main():
    for _ in range(int(input())):
        a = input()
        b = input()
        veta = []
        vetb = []
        veta = subString(a, len(a))
        vetb = subString(b, len(b))
        if len(set(veta)) != len(set(vetb)):
            print("n")
        else:
            print("s")


def subString(Str,n): 
    vet = []
    for Len in range(1,n + 1): 
        for i in range(n - Len + 1): 
            j = i + Len - 1
            for k in range(i,j + 1): 
                vet.append(Str[k]) 
    return vet
             

main()