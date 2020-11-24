import random

karakterler = ("qwertyuıopğüişlkjhgfdsazxcvbnmöçQWERTYUIOPĞÜİŞLKJHGFDSAZXCVBNMÖÇ123456789!'#+$%&")

sayı = ("Kaç adet şifre istersiniz?")
sayı = int(input(sayı))

uzunluk = ("Şifrenizin uzunluğu ne kadar olsun?")
uzunluk = int(input(uzunluk))

for p in range(sayı):
    şifre = " "
    for c in range(uzunluk):
        şifre += random.choice(karakterler)


    print(şifre)
