with open("takımlar.txt", "r", encoding="utf-8") as file:
    galatasaray = list()
    beşiktaş = list()
    fenerbahçe = list()

    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")
        if (satır_elemanları[1] == "Fenerbahçe"):
            fenerbahçe.append(satır + "\n")
        elif (satır_elemanları[1] == "Galatasaray"):
            galatasaray.append(satır + "\n")
        else:
            beşiktaş.append(satır + "\n")
    with open("gs.txt", "w", encoding="utf-8") as file1:
        for i in galatasaray:
            file1.write(i)
    with open("fb.txt", "w", encoding="utf-8") as file2:
        for i in fenerbahçe:
            file2.write(i)
    with open("bjk.txt", "w", encoding="utf-8") as file3:
        for i in beşiktaş:
            file3.write(i)