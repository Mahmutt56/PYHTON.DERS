# İlk 100 Fibonacci sayısını ekrana yazdırma
fibonacci=[1,1]
for i in range(2,100):
    yenisayi=fibonacci[i-2]+fibonacci[i-1]
    fibonacci.append(yenisayi)
for i in fibonacci:
     print(i)

   