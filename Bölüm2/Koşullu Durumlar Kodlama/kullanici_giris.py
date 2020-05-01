print("""
KULLANICI GİRİŞİ
""")
k_adi="EbruSmnc"
sfr=12345
kullanici_adi=input("Kullanıcı Adınızı Giriniz:")
sifre=int(input("Şifrenizi Giriniz:"))
if(kullanici_adi==k_adi and sifre==sfr):
    print("Kullanıcı adı ve şifre DOĞRU.")
else:
    print("BİLGİLER HATALI!!")
