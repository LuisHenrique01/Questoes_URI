def main():
    while True:
        try:
            d, vf, vg = list(map(int, input().split()))
            tw = 12
            x = ((tw*tw)+(d*d))**0.5
            time_f = tw/vf
            time_g = x/vg
            if time_f >= time_g:
                print("S")
            else:
                print("N")
        except EOFError:
            break


if __name__ == "__main__":
    main()