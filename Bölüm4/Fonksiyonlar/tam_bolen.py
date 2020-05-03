print("""
BİR SAYININ TAM BÖLENLERİNİN BULUNMASI..
ÇIKMAK İÇİN q YA BASIN!!!
""")
liste=list()
def bul(sayı):
    for i in range(1,sayı):
        if(sayı%i==0):
            liste.append(i)
    return liste
while True:
    sayı=input("Sayı giriniz:")
    if(sayı=="q"):
        print("Çıkış yapıldı..")
        break
    else:
        sayı=int(sayı)
        print(bul(sayı))