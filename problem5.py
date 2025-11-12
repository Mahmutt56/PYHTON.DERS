import math

sonuc = 1

for i in range(1, 21):  # 1'den 20'ye kadar
    sonuc = sonuc * i // math.gcd(sonuc, i)  # ekok hesabı

print(sonuc)