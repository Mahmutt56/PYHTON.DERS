#max asal bul
sayi=int(input("Lütfen sayıyı giriniz: "))
b=2
max_asal=1
while sayi>1:   
    if sayi%b==0:
        sayi=sayi/b
        maxasal=b
        continue
    b+=1
print(maxasal)

