r, l = tuple(map(int , input().split()))
baloes = l / ((4/3) * (3.1415*(r**3)))
print("%s"%(round(baloes-0.5)))