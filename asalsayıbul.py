sayi=int(input("bir sayı giriniz"))
for i in range(2,sayi):
  if sayi%i ==0:
       print("asal değildir")
       break
  else :
      print("asaldır")
      break

