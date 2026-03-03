"""Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette rea järjekorranumbri
ja iga rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse."""

poem_list = [
    "Hommikul kui üles ärkan,",
    "arvutit ma laual märkan.",
    "Padja, teki viskan maha,",
    "jooksen ruttu compu taha.",
    "Kiirelt sisestan parooli,",
    "kuid juba tuleb minna kooli.",
    "Error tuleb ette siis,",
    "kool on mulle räme piin."
]

def create_file(filename: str, content: list, count_symbol: list) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(len(content)):
            f.write(str(i + 1) + ". " + content[i] + f" ({count_symbol[i]})\n")


def count_symbols(poem: list) -> list:
    count_list = []
    for line in poem:
        count_list.append(len(line))
    return count_list


if __name__ == "__main__":

    poem_list = [
        "Hommikul kui üles ärkan,",
        "arvutit ma laual märkan.",
        "Padja, teki viskan maha,",
        "jooksen ruttu compu taha.",
        "Kiirelt sisestan parooli,",
        "kuid juba tuleb minna kooli.",
        "Error tuleb ette siis,",
        "kool on mulle räme piin."
    ]

    count_symbol = count_symbols(poem_list)
    create_file("luuletus.txt", poem_list, count_symbol)