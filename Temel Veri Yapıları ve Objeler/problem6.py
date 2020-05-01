"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""
a=int(input("a sayısı:"))
b=int(input("b sayısı:"))
hipotenus=a**2+b**2
c=hipotenus**0.5
print("Hipotenüs:{}".format(c))