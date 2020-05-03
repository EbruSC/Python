print("""
ATM MAKİNESİ İŞLEMLER
1 - BAKİYE SORGULAMA
2 - PARA ÇEKME
3 - PARA YATIRMA
ÇIKMAK İÇİN q ya BASIN!!!!
""")
bakiye=5000
while True:
    islem=(input("İşlem Seçiniz:"))
    if(islem=="q"):
        print("İŞLEM SONLANDIRILMIŞTIR..")
    elif(islem=="1"):
        print("Bakiyeniz:",bakiye)

    elif(islem=="2"):
        miktar=int(input("Çekilecek tutarı giriniz:"))
        if(bakiye-miktar<0):
            print("Yetersiz Bakiye!!")
            continue
        bakiye-=miktar
        print("Kalan bakiye:",bakiye)
    elif(islem=="3"):
        miktar = int(input("Yatırılacak tutarı giriniz:"))
        bakiye+=miktar
        print("Yeni bakiye:", bakiye)

    else:
        print("GEÇERSİZ İŞLEM..")