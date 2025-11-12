fibonacci=[1,1]
for i in range(2,10000):
    yenisayi=fibonacci[-2]+fibonacci[-1]
    fibonacci.append(yenisayi)
    if len(fibonacci)==100:
        print(fibonacci)