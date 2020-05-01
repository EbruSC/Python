"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
a=int(input("1.sayıyı giriniz:"))
b=int(input("2.sayıyı giriniz:"))
c=int(input("3.sayıyı giriniz:"))

if(a>c and a>b):
    print("a en büyük sayı:",a)
elif(b>a and b>c):
    print("b en büyük sayı:",b)
elif(c>a and c>b):
    print("c en büyük sayı:",c)