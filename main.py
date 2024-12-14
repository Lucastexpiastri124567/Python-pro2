import random
words = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
print("Bienvenido al creador de contraseñas")
longitud = int(input("eliga la longitud de la que quiere que sea su contraseña:"))
password = ""
for i in range(longitud):
    password += random.choice(words)
print ("la contraseña generada fue:",password)



