from itertools import combinations
nuns = list(map(int, input().split()))
tri = list(set(combinations(nuns, 3)))
forma = False
for a, b, c in tri:
    if (abs(b - c) <  a and a < b + c) and (abs(a - c) < b and b < a + c) and (abs(a - b) < c and c < a + b):
        forma = True
        break
if forma:
    print("S")
else:
    print("N")