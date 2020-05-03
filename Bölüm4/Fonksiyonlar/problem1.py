print("""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını
 dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
ÇIKIŞ İÇİN q YA BASIN!!!
""")

def mukemmel_Sayı(sayı):
    toplam = 0
    for i in range(1,sayı):
        if(sayı%i==0):
            toplam+=i
    if(toplam==sayı):
        return True
    else:
        return False

while True:
    sayı=input("Sayı giriniz:")
    if (sayı == "q"):
        print("Çıkış yapıldı..")
        break
    else:
        sayı = int(sayı)
        print(mukemmel_Sayı(sayı))