print("""
Bu string içerisinde bir harfin kaç defa geçtiğinin belirlenmesi.
""")
string =  "Gökyüzüne kocaman bir dünya ömür sığar."
sozluk = dict()

for karakter in string:
    if (karakter in sozluk):
        sozluk[karakter] += 1
    else:
        sozluk[karakter] = 1
for i,j in sozluk.items():

    print(i,":",j)