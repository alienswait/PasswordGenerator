import random

karakterler = ("qwertyuıopğüişlkjhgfdsazxcvbnmöçQWERTYUIOPĞÜİŞLKJHGFDSAZXCVBNMÖÇ123456789!'#+$%&")

sayı = ("Kaç adet şifre istersiniz?")
sayı = int(input(sayı))

uzunluk = ("Şifrenizin uzunluğu ne kadar olsun?")
uzunluk = int(input(uzunluk))

for i in range(sayı):
    şifre = " "
    for a in range(uzunluk):
        şifre += random.choice(karakterler)


    print(şifre)
