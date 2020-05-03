print("""
KULLANICI GİRİŞİ
(PROGRAM GİRİŞ HAKKI DOLDUĞUNDA VE DOĞRU GİRİŞ YAPILDIĞINDA SONLANMAKTADIR.)
""")
k_adi="EbruSmnc"
sfr=12345
sayac=3
while True: #sonsuz döngüye giriyor
    kullanici_adi=input("Kullanıcı Adınızı Giriniz:")
    sifre=int(input("Şifrenizi Giriniz:"))
    if(kullanici_adi!=k_adi and sifre==sfr and sayac!=0):
        print("Kullanıcı Adı Hatalı!")
        sayac-=1
    elif(kullanici_adi==k_adi and sifre!=sfr and sayac!=0):
        print("Şifre Hatalı!")
        sayac-=1
    elif (kullanici_adi != k_adi and sifre != sfr and sayac != 0):
        print("Kuulanıcı Adı ve Şifre Hatalı!")
        sayac -= 1
    else:
        print("GİRİŞ BAŞARILI..")
        break
    if(sayac==0):
        print("Giriş Hakkınız Bitmiştir!!")
        break

