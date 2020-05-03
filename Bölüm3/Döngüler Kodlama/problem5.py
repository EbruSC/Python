print("""
1'den 100'e kadar olan sayılardan sadece 7'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
""")
for i in range(1, 100):

    if (i % 7 != 0):
        continue
    print(i)