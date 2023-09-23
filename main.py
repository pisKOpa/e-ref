import random
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("sifre girin:"))

parola = ""
for i in range(parola_uzunlugu):

    parola += random.choice(chars)

print (parola)