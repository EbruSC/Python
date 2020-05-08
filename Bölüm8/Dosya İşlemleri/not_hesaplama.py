print("""
sınıfın harf notlarını hesaplayarak kalanları "kalanlar.txt" dosyasında ve geçenleri 
"geçenler.txt" yazdırmak
""")
def not_hesapla(satır):
    satır=satır[:-1]
    liste=satır.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    sonuc=not1*0.3+not2*0.3+not3*0.4
    if(sonuc>=90):
        harf="AA"
    elif(sonuc>=85):
        harf="BA"
    elif(sonuc>=80):
        harf="BB"
    elif (sonuc>=75):
        harf = "CB"
    elif (sonuc>=70):
        harf = "CC"
    elif (sonuc>=65):
        harf = "DC"
    elif (sonuc>=60):
        harf = "DD"
    elif (sonuc>=55):
        harf = "FD"
    else:
        harf="FF"
    return isim+"="+harf

with open("dosya.txt","r",encoding="utf-8") as file:
    liste=list()
    for i in file:
        liste.append(not_hesapla(i))
    print(liste)
    with open("sonuclar.txt", "w", encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)


