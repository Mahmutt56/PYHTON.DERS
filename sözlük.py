metin=(input("bir metin giriniz : "))

sözlük=dict()
for harf in metin:
    if harf in sözlük:
      sözlük[harf]+=1
    else:
       sözlük[harf]=1

print(sözlük)
