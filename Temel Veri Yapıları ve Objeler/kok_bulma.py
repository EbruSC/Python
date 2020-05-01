"""
2.dereceden bir bilinmeyenli denklemin köklerini bulma
Denklem=ax**2+bx+c
delta= b**2-4*a*c
1.kök= (-b-delta**0.5)/(2*a)
2.kök= (-b+delta**0.5)/(2*a)
"""
print("DENKLEM KÖKLERİNİ BULAN PROGRAM\n")
a=int(input("a değeri:"))
b=int(input("b değeri:"))
c=int(input("c değeri:"))
bilinmeyenler=[a,b,c]
delta=b**2-4*a*c
kok1=(-b-delta**0.5)/(2*a)
kok2=(-b+delta**0.5)/(2*a)
kokler=[kok1,kok2]
print("Denklemin kökleri:\nkök1:{}\nkök2:{}\n".format(kokler[0],kokler[1]))
print("İŞLEM BAŞARILI..")