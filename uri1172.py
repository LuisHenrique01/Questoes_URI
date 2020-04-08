def main():
    for i in range(10):
        vetor = int(input())
        if vetor < 1:
            vetor = 1
        print('X[%i] = %i'%(i, vetor))
    
main()