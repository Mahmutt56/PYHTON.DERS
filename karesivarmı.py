#ekrandan okunan bir sayının karesi olup olmadığını kontrol etme 
sayi=int(input("bir sayı giriniz : "))

karekök=sayi**0.5
if karekök==int(karekök):
    print("tam kare" + str(karekök) +   " karesi")
else:
    print("tam kare değil")

