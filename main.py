# Glavna metoda koja pokrece program!
from karta import *
from korisnik import *
from let import *
import datoteka
import time

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
IZVESTAJ_O_PRODATIM_KARTAMA = 2

# opcije pretrage leta
PRETRAGA_LETA_PO_POLAZISTU = 1
PRETRAGA_LETA_PO_ODREDISTU = 2
PRETRAGA_LETA_PO_VREMENU_POLETANJA = 3
PRETRAGA_LETA_PO_VREMENU_SLETANJA = 4
PRETRAGA_LETA_PO_PREVOZNIKU = 5
# izmena karte
KARTA_NE_POSTOJI = 1
# opcije izvestaja o prodatim kartama
PRODATE_KARTE_ZA_IZABRANI_DAN_PRODAJE = 1
PRODATE_KARTE_ZA_IZABRANI_DAN_POLASKA = 2
PRODATE_KARTE_ZA_IZABRANI_DAN_PRODAJE_I_IZABRANOG_PRODAVCA = 3
UKUPAN_BROJ_I_CENA_PRODATIH_KARATA_ZA_IZABRANI_DAN_PRODAJE = 4
UKUPAN_BROJ_I_CENA_PRODATIH_KARATA_ZA_IZABRANI_DAN_POLASKA = 5
UKUPAN_BROJ_I_CENA_PRODATIH_KARATA_ZA_IZABRANI_DAN_PRODAJE_I_IZABRANOG_PRODAVCA = 6
UKUPAN_BROJ_I_CENA_PRODATIH_KARATA_U_POSLEDNJIH_30_DANA_PO_PRODAVCIMA = 7


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
            prikazi_opcije_korisniku(uloga, korisnickoIme, korisnikServis)


def prikazi_opcije_korisniku(uloga, korisnickoIme, korisnikServis):
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
                prikazi_opcije_unosenja_nove_karte(korisnickoIme, korisnikServis)
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
            elif opcija == IZVESTAJ_O_PRODATIM_KARTAMA:
                prikazi_opcije_izvestaja()
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


def prikazi_opcije_unosenja_nove_karte(korisnickoIme, korisnikServis):
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
            KartaServis.prikazi_slobodna_sedista(nazivLeta, datumLeta)
            mesto = input("Unesite slobodno sediste: ")
            imeProdavca = korisnikServis.vrati_ime(korisnickoIme)
            datumIzdavanja = time.strftime("%x")
            novaKarta = Karta(nazivLeta, imePutnika, prezimePutnika, drzavljanstvoPutnika, brojPasosaPutnika, datumLeta,
                              mesto, imeProdavca, datumIzdavanja)
            listaNovihKarata.append(novaKarta)
            Karta.upisi_karte(novaKarta)

        elif opcija == STAMPANJE_UNETIH_NOVIH_KARATA:
            for novaKarta in listaNovihKarata:
                Karta.print_karte(novaKarta)
        else:
            print("Uneli ste nepostojecu opciju.")


def izmena_karte():
    nazivLeta = input("Unesite naziv leta: ")
    brojPasosaPutnika = input("Unesite broj pasosa putnika: ")
    datumLeta = input("Unesite datum leta: ")
    noviNazivLeta = input("Unesite novi naziv leta: ")
    noviDatumLeta = input("Unesite novi datum leta: ")
    KartaServis.prikazi_slobodna_sedista(noviNazivLeta, noviDatumLeta)
    novoSediste = input("Unesite novo sediste: ")
    stariPodaciLista = KartaServis.izmeni_kartu(nazivLeta, brojPasosaPutnika, datumLeta)
    if stariPodaciLista[5] == KARTA_NE_POSTOJI:
        print("Ne postoji karta sa tim podacima.")
    else:
        novaKarta = Karta(noviNazivLeta, stariPodaciLista[0], stariPodaciLista[1], stariPodaciLista[2],
                          brojPasosaPutnika,
                          noviDatumLeta, novoSediste, stariPodaciLista[3], stariPodaciLista[4])
        Karta.upisi_karte(novaKarta)
        print("Karta je izmenjena.")


def brisanje_karte():
    nazivLeta = input("Unesite naziv leta: ")
    brojPasosaPutnika = input("Unesite broj pasosa putnika: ")
    datumLeta = input("Unesite datum leta: ")
    nepostojecaKarta = KartaServis.obrisi_kartu(nazivLeta, brojPasosaPutnika, datumLeta)
    if nepostojecaKarta == True:
        print("Ne postoji karta sa tim podacima.")
    else:
        print("Karta je obrisana.")


def prikazi_opcije_izvestaja():
    print("1 Lista prodatih karata za izabrani dan prodaje.")
    print("2 Lista prodatih karata za izabrani dan polaska.")
    print("3 Lista prodatih karata za izabrani dan prodaje i izabranog prodavca.")
    print("4 Ukupan broj i cena prodatih karata za izabrani dan prodaje.")
    print("5 Ukupan broj i cena prodatih karata za izabrani dan polaska.")
    print("6 Ukupan broj i cena prodatih karata za izabrani dan prodaje i izabranog prodavca.")
    print("7 Ukupan broj i cena prodatih karata u poslednjih 30 dana, po prodavcima.")
    opcija = eval(input("Unesite zeljenu opcija je: "))

    if opcija == PRODATE_KARTE_ZA_IZABRANI_DAN_PRODAJE:
        danProdaje = input("Unesite dan prodaje: ")
        pronadjeneKarte = KartaServis.prodate_karte_za_izabrani_dan_prodaje_ili_polaska(danProdaje,
                                                                                        PRODATE_KARTE_ZA_IZABRANI_DAN_PRODAJE)
        KartaServis.prikazi_karte(pronadjeneKarte)

    elif opcija == PRODATE_KARTE_ZA_IZABRANI_DAN_POLASKA:
        danPolaska = input("Unesite dan polaska: ")
        pronadjeneKarte = KartaServis.prodate_karte_za_izabrani_dan_prodaje_ili_polaska(danPolaska,
                                                                                        PRODATE_KARTE_ZA_IZABRANI_DAN_POLASKA)
        KartaServis.prikazi_karte(pronadjeneKarte)

    elif opcija == PRODATE_KARTE_ZA_IZABRANI_DAN_PRODAJE_I_IZABRANOG_PRODAVCA:
        danProdaje = input("Unesite dan prodaje: ")
        izabraniProdavac = input("Unesite izabranog prodavca: ")
        pronadjeneKarte = KartaServis.prodate_karte_za_izabrani_dan_prodaje_i_izabranog_prodavca(danProdaje,
                                                                                                 izabraniProdavac)
        KartaServis.prikazi_karte(pronadjeneKarte)
    else:
        print("Uneli ste nepostojecu opciju.")


main()
