print("""
FAKTORİYEL HESAPLAMA
Çıkmak için q ya basın..
""")

while True:
    giris=input("Sayı girin:")
    if(giris=="q"):
        print("Çıkış Yapıldı..")
        break
    else:
        sayı = int(giris)
        faktoriyel=1
        for i in range(1,sayı+1):
            faktoriyel*=i
        print("Faktoriyel:",faktoriyel)
