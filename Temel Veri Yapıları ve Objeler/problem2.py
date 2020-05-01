"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
boy=float(input("boy bilgisi:")) #1.68
kilo=int(input("kilo bilgisi:"))
sonuc=kilo/(boy**2)
print("sonuc:{}".format(sonuc))