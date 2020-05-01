print("""
********************
---Hesap Makinesi---
İşlemler:
1 - Toplama İşlemi
2 - Çıkartma İşlemi
3 - Çarpma İşlemi
4 - Bölme İşlemi
********************
""")
a=int(input("1.sayıyı giriniz:"))
b=int(input("2.sayıyı giriniz:"))
islemno=int(input("İşlem numarası seçiniz:"))

if(islemno==1):
    print("Toplamı:",a+b)
elif(islemno==2):
    print("Çıkarımı:{}".format(a-b))
elif(islemno==3):
    print("Çarpım:{}",a*b)
elif(islemno==4):
    print("Bölüm:{}".format(a/b))
else:
    print("HATALI SEÇİM!!")