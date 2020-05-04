print("""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu değeri 
dönsün. Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar 
bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
""")


def kontrol(sayı):
    if(sayı%2==0):
        return sayı
    else:
        raise ValueError


liste = [8,1,12,75,15,49,62,75,32]

for i in liste:
    try:
        print("Çift:",kontrol(i))

    except ValueError:
        print("Fonksiyonda ValueError hatası oluştu!!")
        continue
