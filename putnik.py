#putnik
#Putnik ima :Ime, prezime, drzavljanstvo, pasos.

korisnici = open("korisnici.txt", "r")
koris = korisnici.readline()
korisniciLista = koris.split("|")
print(koris)
print(korisniciLista)