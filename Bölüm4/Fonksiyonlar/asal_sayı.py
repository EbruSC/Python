print("""
ASAL SAYI: SADECE KENDİSİNE VE 1 E BÖLÜNEBİLEN SAYILARDIR.
ÇIKMAK İÇİN q YA BASIN!!!
""")
def asal_sayı(sayı):
    if(sayı==2):
        print("Asaldır..")

    elif(sayı==1):
        print("Asal Değildir..")

    else:
        for i in range(2,sayı):
            if(sayı%i==0):
                print("Asal Değildir..")
                break
        print("Asaldır..")

while True:
    sayı=input("Sayı giriniz:")
    if(sayı=="q"):
        print("Çıkış Yapılıyor..")
        break
    else:
        sayı=int(sayı)
        asal_sayı(sayı)


