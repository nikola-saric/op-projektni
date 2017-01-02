# main
import korisnik


def ulogovanje():
    ul = 0

    while True:
        print("Ulogujte se:")
        imeProvera = input("Unesite vase korisnicko ime: ")
        lozinkaProvera = input("Unesite vasu lozinku: ")

        # provera korisnickog imena:
        korisnici = open("korisnici", "r")
        kor = korisnici.readlines()
        ime = []
        nIme = len(kor)
        for i in range(nIme):
            osobe = (kor[i])
            osobelista = osobe.split("|")
            ime.append(osobelista[0])
        brojImena = len(ime)
        indexKorisnika = -1
        
        for i in range(brojImena):
            if imeProvera == ime[i]:
                indexKorisnika = i


        # provera odgovarajuce lozinke
        lozinka = open("lozinke", "r")
        loz = lozinka.readline()
        lozinke = loz.split("|")

        # uporedjivanje korisnickog imena i lozinke:
        if (indexKorisnika != -1) and (lozinkaProvera == lozinke[indexKorisnika]):

            noviKorisnik = korisnik.Korisnik()
            print("\nUspesno ste se ulogovali!")
            noviKorisnik.informacije(indexKorisnika)
            ul = noviKorisnik.info(indexKorisnika)

            return ul


        else:
            print("Uneli ste pogresno korisnicko ime ili lozinku.")

