#polindromu bulma en büyük
büyük=0
carpanlar=(0,0)

for a in range(100,1000):
    for b in range(a,1000):
        carpim=a*b
        if str(carpim )==str(carpim)[::-1]:
            if carpim>büyük:
                 büyük=carpim
                 carpanlar=(a,b)

print(büyük)
print(carpanlar)

        

