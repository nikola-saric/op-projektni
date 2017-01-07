# Glavna metoda koja pokrece program!
from korisnik import *
from let import *

def main():
    prikaziLoginOpcije()

def prikaziLoginOpcije():
    ulogovan = False
    korisnikServis = KorisnikServis()

    while ulogovan == False:
        print("Ulogujte se:")
        korisnickoIme = input("Unesite vase korisnicko ime: ")
        lozinka = input("Unesite vasu lozinku: ")

        loginUspesan = korisnikServis.login(korisnickoIme, lozinka)
        if loginUspesan == False:
            print("Uneli ste pogresno korisnicko ime ili lozinku.")

        else:
            print("Uspesno ste se ulogovali na sistem.")
            uloga = korisnikServis.vratiUlogu(korisnickoIme)
            print("Vasa uloga je: ", uloga)
            ulogovan = True
            prikaziOpcijeKorisniku(uloga)

def prikaziOpcijeKorisniku(uloga):
    PRETRAGA_LETOVA = 1
    LOG_OUT_KORISNIK = 5
    LOG_OUT_MENADZER = 3
    GASENJE_PROGRAMA_KORISNIK = 6
    GASENJE_PROGRAMA_MENADZER = 4
    opcija = 0
    letServis = LetServis()

    if uloga == "prodavac":
        while opcija != LOG_OUT_KORISNIK:
            print("1 Pretrazite letove.")
            print("2 Unesite novu kartu.")
            print("3 Izmenite postojecu kartu.")
            print("4 Obrisite postojecu kartu.")
            print("5 Izlogujte se.")
            print("6 Ugasite program.")
            opcija = eval(input("Unesite zeljenu opciju: "))
            if opcija == PRETRAGA_LETOVA:
                prikaziOpcijePretrageLetova(letServis)
            elif opcija == LOG_OUT_KORISNIK:
                prikaziLoginOpcije()
            elif opcija == GASENJE_PROGRAMA_KORISNIK:
                break

    elif uloga == "menadzer":
        while opcija != LOG_OUT_MENADZER:
            print("1 Pretrazite letove.")
            print("2 Izvestaj o prodatim kartama.")
            print("3 Izlogujte se.")
            print("4 Ugasite program.")
            opcija = eval(input("Unesite zeljenu opciju: "))
            if opcija == LOG_OUT_MENADZER:
                prikaziLoginOpcije()
            elif opcija == GASENJE_PROGRAMA_MENADZER:
                break

def prikaziOpcijePretrageLetova(letServis):
    PRETRAGA_LETA_PO_POLAZISTU = 1

    print("1 Pretrazite po polazistu.")
    print("2 Pretrazite po odredistu.")
    print("3 Pretrazite po vremenu poletanja.")
    print("4 Pretrazite po vremenu sletanja.")
    print("5 Pretrazite po prevozniku.")
    opcija = eval(input("Unesite zeljenu opciju: "))

    if opcija == PRETRAGA_LETA_PO_POLAZISTU:
        polaziste = input("Unesite polaziste: ")
        rezultatPretrage = letServis.pretragaLeta(polaziste, LetServis.OPCIJA_PRETRAGE_POLAZISTE)
        for let in rezultatPretrage:
            print(let)
main()
