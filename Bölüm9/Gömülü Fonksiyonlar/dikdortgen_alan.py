print("""
Dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.
 [(3,4),(10,3),(5,6),(1,9)]
 sonuc: [12, 30, 30, 9]
""")


def alan(demet):
    return demet[0]*demet[1]
liste= [(3,4),(10,3),(5,6),(1,9)]

print(list(map(alan,liste)))


