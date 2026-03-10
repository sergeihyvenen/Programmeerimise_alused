"""
Ülesanne. Kaugushüpe
Noorte kaugushüppe võistlusel sai täita meistrivõistluste normatiivi. Juhtus aga, et mõõteseade muutis kõiki tulemusi ühe ja sama arvu sentimeetrite võrra. Õnneks olid tulemused faili salvestatud ja nüüd sai arvutades leida tegelikud tulemused.
Selleks, et edaspidi saaks selliseid olukordi kiiremini lahendada, otsustati tellida programm, mis lisaks tulemuste korrigeerimisele leiab ka normatiivi täitnud tegelike tulemuste arvu ning nende aritmeetilise keskmise.
Koostada funktsioon, mis võtab argumentideks vigase tulemuse (meetrites) ja mõõteparanduse (sentimeetrites). Funktsioon arvutab tegeliku tulemuse (meetrites) ning tagastab selle.
tegelikTulemus = viganeTulemus + mõõteparandus / 100
Koostada programm, mis küsib kasutajalt:
•	failinime,
•	mõõteparanduse (nt 35 näitab, et igale tulemusele tuleb liita 35 sentimeetrit (e 0,35 meetrit)),
•	meistrivõistluste normatiivi.
Programm peab
•	lugema failist vigased tulemused (meetrites);
•	funktsiooniga arvutama tegelikud tulemused ja väljastama need ekraanile (ümardatuna kahe kümnendkohani pärast koma);
•	arvutama ja väljastama ekraanile normatiivi täitnud tegelike tulemuste arvu ja nende keskmise (ümardatuna kahe kümnendkohani pärast koma).
o	Kui normatiivi täitjaid ei ole, siis keskmist ei arvutata ega väljastata.
Näide programmi tööst
Faili kaugus.txt sisu:
6.56
5.76
5.82
5.23
5.74
6.14
5.28
5.77
6.45
6.02
5.78

Programmi töö:
Sisestage failinimi: kaugus.txt
Sisestage parandus sentimeetrites: 35
Sisestage meistrivõistluste normatiiv meetrites: 6.45
Tegelikud tulemused
6.91
6.11
6.17
5.58
6.09
6.49
5.63
6.12
6.8
6.37
6.13
Normatiivi täitis 3.
Täitnute keskmine on 6.73.


"""

def real_result(wrong_result, correction):
    return wrong_result + correction / 100


def main():
    filename = input("Enter file name: ")
    correction = float(input("Enter correction in centimeters: "))
    norm = float(input("Enter championship qualification in meters: "))

    qualified = []

    with open(filename, encoding="utf-8") as f:
        for line in f:
            wrong = float(line.strip())
            real = real_result(wrong, correction)

            print(round(real, 2))

            if real >= norm:
                qualified.append(real)

    print("Qualified:", len(qualified))

    if len(qualified) > 0:
        avg = round(sum(qualified) / len(qualified), 2)
        print("Average of qualified:", avg)


if __name__ == "__main__":
    main()