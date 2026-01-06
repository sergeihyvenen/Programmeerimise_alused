"""On selge, et auto kiiruse tõstmine vähendab sõidule kuluvat aega
ehk ma jõuame varem sihtpunkti. Kui palju me aga ajas võidame? Koostage programm,
mis küsib käivitamisel läbitava vahemaa pikkust (kilomeetrites, see kehtib kogu programmitöö aja),
seejärel aga küsib kasutajalt korduvalt kiirust (km/h) ning väljastab selle põhjal korrektse lausega sõiduks
kuluva aja ja erinevuse eelmisest tulemusest.
Kui kasutaja uut kiirust ei sisesta, vaid vajutab lihtsalt sisestusklahvile,
siis katkestatakse tsükkel ja tänatakse kasutajat."""

def car():
    vahemaa = float(input("Sisesta läbitav vahemaa km: "))

    eelmine_aeg = None

    while True:
        sisend = input("Sisesta kiirus km/h. Lõpetamiseks vajuta Enter: ")

        if sisend == "":
            print("Aitäh! Programm lõpetatud.")
            break

        try:
            kiirus = float(sisend)
            if kiirus <= 0:
                print("Kiirus peab olema suurem kui 0 km/h.")
                continue
        except ValueError:
            print("Palun sisesta korrektne number.")
            continue

        aeg_h = vahemaa / kiirus

        tunnid = int(aeg_h)
        minutid = int(round((aeg_h - tunnid) * 60))

        print(f"Sõiduks kulub {tunnid} tundi ja {minutid} minutit.")

        if eelmine_aeg is not None:
            vahe = eelmine_aeg - aeg_h
            vahe_tunnid = int(vahe)
            vahe_minutid = int(round((vahe - vahe_tunnid) * 60))
            print(f"Selle võrra on aeg vähenenud: {vahe_tunnid} tundi ja {vahe_minutid} minutit.")

        eelmine_aeg = aeg_h


if __name__ == "__main__":
    car()