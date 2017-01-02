# Glavna metoda koja pokrece program!
import ulogovanje
import letovi



def main():
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
                print("Izabrali ste 2")

            elif vasIzbor == 2:
                print("Izabrali ste 3")

            elif vasIzbor == 2:
                print("Izabrali ste 4")

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
