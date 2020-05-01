"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı
bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
tl=int(input(" t1 TL harcanan:")) #2 tl int tipinde
tl2=float(input("t2 TL harcanan:")) #0.22 tl float tipinde
mesafe=int(input("gidilen km:")) #300 km
tutar=tl*mesafe
tutar2=tl2*mesafe
print("Tutar:{}\n Tutar2:{}".format(tutar,tutar2))