"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""
boy=float(input("Boy giriniz:"))
kilo=int(input("Kilo giriniz:"))
sonuc=kilo/(boy**2)
print("BKİ:\n",sonuc)
if(sonuc<18.5):
    print("ZAYIF")
elif(sonuc>18.5 and sonuc<25):
    print("NORMAL")
elif(sonuc>25 and sonuc<30):
    print("FAZLA KİLOLU")
else:
    print("OBEZ")