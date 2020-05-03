print("""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
 Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
""")
toplam=0
while True:
    sayı=int(input("Sayı giriniz:"))
    for i in range(1,sayı):
        if(sayı%i==0):
            print(i)
            toplam+=i
    if(toplam==sayı):
        print("Mükemmel Sayı..")
    else:
        print("Mükemmel Sayı Değil!!")