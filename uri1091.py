def main():
    while True:
        rep = int(input())
        if rep == 0: break
        div_x, div_y = list(map(int, input().split())) 
        for _ in range(rep):
            ponto_x, ponto_y = list(map(int, input().split()))
            if ponto_x == div_x or ponto_y == div_y:
                print('divisa')
            elif ponto_x > div_x and ponto_y > div_y:
                print('NE')
            elif ponto_x > div_x and ponto_y < div_y:
                print('SE')
            elif ponto_x < div_x and ponto_y > div_y:
                print('NO')
            else:
                print('SO')


if __name__ == "__main__":
    main()

