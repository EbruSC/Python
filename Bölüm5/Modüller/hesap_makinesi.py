print("""
Math modülündeki hazır fonksiyonlar ile hesap makinesi uygulaması
İŞLEMLER
1 - 'factorial'
2 - 'log10'
3 - 'pow'
4 - 'sqrt'
""")
import math
sayı=int(input("Sayı girin:"))

while True:
    islem=int(input("İşlem Seçiniz:"))
    if(islem==1):
        print(math.factorial(sayı))
    elif(islem==2):
        print(math.log10(sayı))
    elif(islem==3):
        print(math.pow(sayı,2))
    elif(islem==4):
        print(math.sqrt(sayı))
    else:
        print("Hatalı İşlem Seçimi!!")
        break