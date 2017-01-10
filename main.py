# Glavna metoda koja pokrece program!
from korisnik import *
from let import *
from karta import *

# osnovne opcije programa
PRETRAGA_LETOVA = 1
UNOSENJE_NOVE_KARTE = 2
IZMENA_KARTE = 3
BRISANJE_KARTE = 4
LOG_OUT_KORISNIK = 5
LOG_OUT_MENADZER = 3
GASENJE_PROGRAMA_KORISNIK = 6
GASENJE_PROGRAMA_MENADZER = 4
UNOSENJE_NOVIH_KARATA = 1
STAMPANJE_UNETIH_NOVIH_KARATA = 2

# opcije pretrage leta
PRETRAGA_LETA_PO_POLAZISTU = 1
PRETRAGA_LETA_PO_ODREDISTU = 2
PRETRAGA_LETA_PO_VREMENU_POLETANJA = 3
PRETRAGA_LETA_PO_VREMENU_SLETANJA = 4
PRETRAGA_LETA_PO_PREVOZNIKU = 5

def main():
    prikazi_login_opcije()

def prikazi_login_opcije():
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
            uloga = korisnikServis.vrati_ulogu(korisnickoIme)
            print("Vasa uloga je: ", uloga)
            ulogovan = True
            prikazi_opcije_korisniku(uloga)

def prikazi_opcije_korisniku(uloga):
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
                prikazi_opcije_pretrage_letova(letServis)
            elif opcija == UNOSENJE_NOVE_KARTE:
                prikazi_opcije_unosenja_nove_karte()
            elif opcija == IZMENA_KARTE:
                izmena_karte()
            elif opcija == BRISANJE_KARTE:
                brisanje_karte()
            elif opcija == LOG_OUT_KORISNIK:
                prikazi_login_opcije()
            elif opcija == GASENJE_PROGRAMA_KORISNIK:
                break
            else:
                print("Uneli ste nepostojecu opciju.")

    elif uloga == "menadzer":
        while opcija != LOG_OUT_MENADZER:
            print("1 Pretrazite letove.")
            print("2 Izvestaj o prodatim kartama.")
            print("3 Izlogujte se.")
            print("4 Ugasite program.")
            opcija = eval(input("Unesite zeljenu opciju: "))
            if opcija == PRETRAGA_LETOVA:
                prikazi_opcije_pretrage_letova(letServis)
            elif opcija == LOG_OUT_MENADZER:
                prikazi_login_opcije()
            elif opcija == GASENJE_PROGRAMA_MENADZER:
                break
            else:
                print("Uneli ste nepostojecu opciju.")


def prikazi_opcije_pretrage_letova(letServis):
    print("1 Pretrazite po polazistu.")
    print("2 Pretrazite po odredistu.")
    print("3 Pretrazite po vremenu poletanja.")
    print("4 Pretrazite po vremenu sletanja.")
    print("5 Pretrazite po prevozniku.")
    opcija = eval(input("Unesite zeljenu opciju: "))

    if opcija == PRETRAGA_LETA_PO_POLAZISTU:
        polaziste = input("Unesite polaziste: ")
        rezultatPretrage = letServis.pretraga_leta(polaziste, LetServis.OPCIJA_PRETRAGE_POLAZISTE)
        for let in rezultatPretrage:
            print(let)

    elif opcija == PRETRAGA_LETA_PO_ODREDISTU:
        odrediste = input("Unesite odrediste: ")
        rezultatPretrage = letServis.pretraga_leta(odrediste, letServis.OPCIJA_PRETRAGE_ODREDISTE)
        for let in rezultatPretrage:
            print(let)

    elif opcija == PRETRAGA_LETA_PO_VREMENU_POLETANJA:
        vremePoletanja = input("Unesite vreme poletanja: ")
        rezultatPretrage = letServis.pretraga_leta(vremePoletanja, letServis.OPCIJA_PRETRAGE_VREME_POLETANJA)
        for let in rezultatPretrage:
            print(let)

    elif opcija == PRETRAGA_LETA_PO_VREMENU_SLETANJA:
        vremeSletanja = input("Unesite vreme sletanja: ")
        rezultatPretrage = letServis.pretraga_leta(vremeSletanja, letServis.OPCIJA_PRETRAGE_VREME_SLETANJA)
        for let in rezultatPretrage:
            print(let)

    elif opcija == PRETRAGA_LETA_PO_PREVOZNIKU:
        prevoznik = input("Unesite naziv prevoznika: ")
        rezultatPretrage = letServis.pretraga_leta(prevoznik, letServis.OPCIJA_PRETRAGE_PREVOZNIKU)
        for let in rezultatPretrage:
            print(let)
    else:
        print("Uneli ste nepostojecu opciju.")


def prikazi_opcije_unosenja_nove_karte():
    opcija = 0
    listaNovihKarata = []

    while opcija != STAMPANJE_UNETIH_NOVIH_KARATA:
        print("1 Unesite novu kartu: ")
        print("2 Odstampajte nove unete karte: ")
        opcija = eval(input("Unesite zeljenu opciju: "))
        if opcija == UNOSENJE_NOVIH_KARATA:
            nazivLeta = input("Unesite naziv leta: ")
            imePutnika = input("Unesite ime putnika: ")
            prezimePutnika = input("Unesite prezime putnika: ")
            drzavljanstvoPutnika = input("Unesite drzavljanstvo putnika: ")
            brojPasosaPutnika = input("Unesite broj pasosa putnika: ")
            datumLeta = input("Unesite datum leta: ")
            novaKarta = Karta(nazivLeta, imePutnika, prezimePutnika, drzavljanstvoPutnika, brojPasosaPutnika, datumLeta)
            listaNovihKarata.append(novaKarta)

        elif opcija == STAMPANJE_UNETIH_NOVIH_KARATA:
            for novaKarta in listaNovihKarata:
                Karta.upisi_karte(novaKarta)
                Karta.print_karte(novaKarta)
        else:
            print("Uneli ste nepostojecu opciju.")


def izmena_karte():
    nazivLeta = input("Unesite naziv leta: ")
    brojPasosaPutnika = input("Unesite broj pasosa putnika: ")
    datumLeta = input("Unesite datum leta: ")
    noviNazivLeta = input("Unesite novi naziv leta: ")
    noviDatumLeta = input("Unesite novi datum leta: ")
    stariPodaciLista = KartaServis.izmeni_kartu(nazivLeta, brojPasosaPutnika, datumLeta)
    novaKarta = Karta(noviNazivLeta, stariPodaciLista[0], stariPodaciLista[1], stariPodaciLista[2], brojPasosaPutnika,
                      noviDatumLeta)
    Karta.upisi_karte(novaKarta)


def brisanje_karte():
    nazivLeta = input("Unesite naziv leta: ")
    brojPasosaPutnika = input("Unesite broj pasosa putnika: ")
    datumLeta = input("Unesite datum leta: ")
    KartaServis.obrisi_kartu(nazivLeta, brojPasosaPutnika, datumLeta)

main()
