lista = [input() for i in range(int(input()))]
se = set(lista)
if len(se) != len(lista):
    print("1")
else: 
    print('0')