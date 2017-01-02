# File se koristi samo za testiranje raznih opcija...

class Let:
    letovi = []

    def __init__(self, brojLeta, polaziste, odrediste, vremePol, vremeSlet, prevoznik, dan, modelAv, cena):
        letovi = []
        brLeta = 4
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


print(Let)
