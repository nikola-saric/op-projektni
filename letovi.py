# Sve u vezi letova

class Let:
    letovi = []

    def __init__(self, brojLeta, polaziste, odrediste, vremePol, vremeSlet, prevoznik, dan, modelAv, cena, BrLeta):
        letovi = []
        letoviFile = open("letovi.txt", "r")
        letoviRF = letoviFile.readlines()
        brojRedova = len(letoviRF)
        for brLeta in range(brojRedova):
            jedanLet = letoviFile.readline(brLeta)
            noviLet = jedanLet.split("|")
            letovi.append(noviLet)


        letovi[0] = brojLeta
        letovi[1] = polaziste
        letovi[2] = odrediste
        letovi[3] = vremePol
        letovi[4] = vremeSlet
        letovi[5] = prevoznik
        letovi[6] = dan
        letovi[7] = modelAv
        letovi[8] = cena




def pretragaLetova(izborPretrage):
    if izborPretrage == 1:
        letoviFile = open("letovi.txt", "r")
        letRL = letoviFile.readlines()
        letoviLista = []
        lenLet = len(letRL)
        for i in range(lenLet):
            letovi = (letRL[i])
            let = letovi.split("|")
            letoviLista.append(let[1])
        lenLL = len(letoviLista)
        polaziste = input("Unesite polaziste: ")

        for i in range(lenLL):
            if polaziste == letoviLista[i]:
                print(letRL[i])

    elif izborPretrage == 2:
        letoviFile = open("letovi.txt", "r")
        letRL = letoviFile.readlines()
        letoviLista = []
        lenLet = len(letRL)
        for i in range(lenLet):
            letovi = (letRL[i])
            let = letovi.split("|")
            letoviLista.append(let[2])
        lenLL = len(letoviLista)
        polaziste = input("Unesite odrediste: ")

        for i in range(lenLL):
            if polaziste == letoviLista[i]:
                print(letRL[i])

    elif izborPretrage == 3:
        letoviFile = open("letovi.txt", "r")
        letRL = letoviFile.readlines()
        letoviLista = []
        lenLet = len(letRL)
        for i in range(lenLet):
            letovi = (letRL[i])
            let = letovi.split("|")
            letoviLista.append(let[3])
        lenLL = len(letoviLista)
        polaziste = input("Unesite vreme poletanja: ")

        for i in range(lenLL):
            if polaziste == letoviLista[i]:
                print(letRL[i])

    elif izborPretrage == 4:
        letoviFile = open("letovi.txt", "r")
        letRL = letoviFile.readlines()
        letoviLista = []
        lenLet = len(letRL)
        for i in range(lenLet):
            letovi = (letRL[i])
            let = letovi.split("|")
            letoviLista.append(let[4])
        lenLL = len(letoviLista)
        polaziste = input("Unesite vreme sletanja: ")

        for i in range(lenLL):
            if polaziste == letoviLista[i]:
                print(letRL[i])

    elif izborPretrage == 5:
        letoviFile = open("letovi.txt", "r")
        letRL = letoviFile.readlines()
        letoviLista = []
        lenLet = len(letRL)
        for i in range(lenLet):
            letovi = (letRL[i])
            let = letovi.split("|")
            letoviLista.append(let[5])
        lenLL = len(letoviLista)
        polaziste = input("Unesite naziv prevoznika: ")

        for i in range(lenLL):
            if polaziste == letoviLista[i]:
                print(letRL[i])

    else:
        print("Izabrali ste nepostojecu opciju.")
