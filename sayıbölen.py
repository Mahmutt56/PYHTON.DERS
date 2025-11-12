sayi=int(input("bir sayı giriniz"))
pozitifbölen=0
for i in range(1,sayi+1):
    if sayi%i==0:
        pozitifbölen+=1


print("{} sayısının {} tane pozitif böleni vardır".format(sayi,pozitifbölen))
 