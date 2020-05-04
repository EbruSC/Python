print(
"""
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.
"""
)
class Bilgisayar():
    def __init__(self,pc_durum="Uyku",):
        self.pc_durum=pc_durum
    def pc_ac(self):
        if(self.pc_durum=="Açık"):
            print("Bilgisayar zaten açık.")
        else:
            print("Bilgisayar açılıyor...")
            self.pc_durum="Açık"
    def pc_kapat(self):
        if(self.pc_durum=="Kapalı"):
            print("Bilgisayar zaten kapalı.")
        else:
            print("Bilgisayar kapanıyor...")
            self.pc_durum=="Kapalı"
    def pc_uyku(self):
        if(self.pc_durum=="Uyku"):
            print("Bilgisayar zaten uyku modunda.")
        else:
            print("Bilgisayar uyku moduna alınıyor...")
            self.pc_durum=="Uyku"
    def __str__(self):
        return "Pc Durumu:{}".format(self.pc_durum)
bilgisayar=Bilgisayar()
print("""
Bilgisayar Bilgileri
1 - Bilgisayar Aç
2 - Bilgisayar Kapat
3 - Uyku
4 - Bilgisayar Durum Bilgisi
5 - Çıkış

""")
while True:
    işlem=input("İşlem Seçiniz:")
    if(işlem=='5'):
        print("Program Sonlandırıldı!!!")
        break

    if(işlem=="1"):
        bilgisayar.pc_ac()
    elif(işlem=="2"):
        bilgisayar.pc_kapat()
    elif(işlem=="3"):
        bilgisayar.pc_uyku()
    elif (işlem == "4"):
        print(bilgisayar)
    else:
        print("Geçersiz İşlem!!!")