import random
import time
print("""
*****SAYI TAHMİN OYUNU*****
1-50 arasında sayı tahmini
""")

rast_sayı=random.randint(1,50)
tahmin_hakkı=10
while True:
    tahmin=int(input("Sayı girin:"))
    if(tahmin<rast_sayı):
        print("Bekleyiniz..")
        time.sleep(1)
        print("Daha büyük bir sayı girin..")
        tahmin_hakkı-=1
    elif(tahmin>rast_sayı):
        print("Bekleyiniz..")
        time.sleep(1)
        print("Daha küçük bir sayı girin..")
    else:
        print("Bilgiler Sorgulanıyor..")
        time.sleep(1)
        print("Tebrikler..")
        break
    if(tahmin_hakkı==0):
        print("Tahmin Hakkınız Bitti!")
        break