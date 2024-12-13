import random as r, string as s

elemen = s.ascii_letters + s.ascii_lowercase + s.ascii_uppercase + s.digits + s.punctuation
pasword = ""
largo = int(input("cuantos caracteres tendra la contraseña: "))

for i in range (largo):
    pasword += r.choice(elemen)
#esto es una prueba
print(pasword)