#3 basamaklı sayıların kaç tanesi ramaknlarının küplerinin toplamına eşittir python
toplam =0
for i in range(100,1000):
    a=i//100
    b=(i//10)%10
    c=i%10
    if i== a**3 + b**3 + c**3 :
        print(i)
        toplam+=1
print(toplam)       
