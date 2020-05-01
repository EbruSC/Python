"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

"""
a=int(input("1.sayı:"))
b=int(input("2.sayı:"))
print("BEFORE\n")
print("a:{},b:{}\n".format(a,b))
temp=a #temp değişkeni kullanmadan a,b=b,a işlemi ile de değişim gerçekleştirilir.
a=b
b=temp
print("AFTER\n")
print("a:{},b:{}".format(a,b))