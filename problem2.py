    #4 milyondan küçük fibonacci sayıların çift olanların toplamı
fibonacci=[1,1]
i=2
while True:
  if fibonacci[i-1]+fibonacci[i-2] <4000000:
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    i+=1

  else:
    break
toplam=0
for i in fibonacci:
  if i%2==0:
    toplam+=i

print(toplam)




   
