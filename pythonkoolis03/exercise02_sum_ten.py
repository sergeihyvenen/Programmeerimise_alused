"""Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta,
 vaid vajutab lihtsalt sisestusklahvi. Proovige seda ülesannet lahendada nii while- kui for-tsükliga."""

if __name__ == '__main__':
    summa = 0
    for i in range(10):
        arv = float(input(f"Sisesta arv {i + 1}/10: "))
        summa += arv
    i = 11
    while True:
        sisestus = input(f"Sisesta arv {i} (või vajuta Enter lõpetamiseks): ")
        if sisestus == "":
            break
        arv = float(sisestus)
        summa += arv
        i += 1
    print(f"Arvude summa: {summa}")