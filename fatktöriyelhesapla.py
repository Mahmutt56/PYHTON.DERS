#sayi=int(input("bir sayı giriniz"))
#faktöriyel=1
#for i in range(1,sayi+1):
     #faktöriyel *=i
     
#print("{}! = {}".format(sayi,faktöriyel))

#********* while döngüsü ile ************

sayi=int(input("bir sayı giriniz"))
faktöriyel=1
i=1
while i<=sayi:
    faktöriyel*=i
    i+=1

print(f"{sayi}!= {faktöriyel}")    


