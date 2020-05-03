print("""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir
 değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
""")
toplam=0
while True:
    giris=input("sayı giriniz:")

    if(giris=="q"):
        print("Toplam:",toplam)
        print("Çıkış Yapılıyor...")
    else:
        sayı = int(giris)
        print(toplam,"+",sayı)
        toplam+=sayı
