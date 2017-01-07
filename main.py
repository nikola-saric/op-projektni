# Glavna metoda koja pokrece program!
import ulogovanje
import letovi
import karte


def main():
    listaKarata = []
    uloga = ulogovanje.ulogovanje()
    if uloga == "prodavac":
        vasIzbor = 0

        while vasIzbor != 5:
            print("1 Pretrazite letove.")
            print("2 Unesite novu kartu.")
            print("3 Izmenite postojecu kartu.")
            print("4 Obrisite postojecu kartu.")
            print("5 Izlogujte se.")
            vasIzbor = eval(input("Unesite zeljenu opciju: "))

            if vasIzbor == 1:
                print("1 Pretrazite po polazistu.")
                print("2 Pretrazite po odredistu.")
                print("3 Pretrazite po vremenu poletanja.")
                print("4 Pretrazite po vremenu sletanja.")
                print("5 Pretrazite po prevozniku.")
                izborPretrage = eval(input("Unesite zeljenu opciju: "))
                letovi.pretragaLetova(izborPretrage)

            elif vasIzbor == 2:
                noviIzbor = 0
                while noviIzbor != 2:
                    print("1 Rezervisite novu kartu.")
                    print("2 Odstampajte rezervisane karte")
                    noviIzbor = eval(input("Unesite zeljenu opciju: "))

                    if noviIzbor == 1:
                        nazivLeta = input("Unesite naziv leta: ")
                        vremIOdredList = karte.Karta.proveraVremena(nazivLeta)
                        polaziste = vremIOdredList[0]
                        vreme = vremIOdredList[1]

                        imePutnika = input("Unesite ime putnika: ")
                        prezimePutnika = input("Unesite prezime putnika: ")
                        drzavPutnika = input("Unesite drzavljanstvo putnika: ")
                        brojPasosaPutnika = input("Unesite broj pasosa putnika: ")

                        novaKarta = karte.Karta(nazivLeta, imePutnika, prezimePutnika, drzavPutnika, brojPasosaPutnika)
                        listaKarata.append(novaKarta)

                    elif noviIzbor == 2:
                        for i in listaKarata:
                            karte.Karta.printKarte(i)

                    else:
                        print("Izabrali ste nepostojecu opciju.")

            elif vasIzbor == 3:
                print("Izabrali ste 3")

            elif vasIzbor == 4:
                brLeta = input("Unesite broj leta: ")
                #brPasosa = input("Unesite broj pasosa: ")

                for i in listaKarata:
                    if novaKarta.nazivLeta == brLeta:
                        listaKarata.remove(i)
                        print(i)
                    else:
                        print(i)


            elif vasIzbor == 5:
                break

            else:
                print("Izabrali ste nepostojecu opciju.")

    elif uloga == "menadzer":
        vasIzbor = 0
        while vasIzbor != 3:
            print("1 Pretrazite letove.")
            print("2 Izvestaj o prodatim kartama.")
            print("3 Izlogujte se.")
            vasIzbor = eval(input("Unesite zeljenu opciju: "))
            if vasIzbor == 1:
                print("1 Pretrazite po polazistu.")
                print("2 Pretrazite po odredistu.")
                print("3 Pretrazite po vremenu poletanja.")
                print("4 Pretrazite po vremenu sletanja.")
                print("5 Pretrazite po prevozniku.")
                izborPretrage = eval(input("Unesite zeljenu opciju: "))
                letovi.pretragaLetova(izborPretrage)

            elif vasIzbor == 2:
                print("Izabrali ste 2")

            elif vasIzbor == 3:
                break

            else:
                print("Izabrali ste nepostojecu opciju.")


main()
