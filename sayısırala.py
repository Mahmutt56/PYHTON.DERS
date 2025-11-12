# ekrandan peş peşe okunan 5 sayı en küçüğü ve en büyüğü ekrana yadır
list=[]
for i in range(5):
    sayi=int(input("bir sayı giriniz : "))
    list.append(sayi)

print(f"en büyük sayı: {max(list)}")
print(f"en küçük sayı: {min(list)}")


