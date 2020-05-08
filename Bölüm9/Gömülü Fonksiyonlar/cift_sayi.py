print("""
[1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazalım.
""")
from functools import reduce

liste=[1,2,3,4,5,6,7,8,9,10]

liste1=list(filter(lambda x:x%2==0,liste))
print(reduce(lambda x,y:x+y,liste1))
