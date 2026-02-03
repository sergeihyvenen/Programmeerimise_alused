""" Koosta programm, mis "viskab täringut" kolm korda ehk väljastab ekraanile 3 juhusliku täringuviske tulemused.
Et ekraanipilt oleks realistlikum, esita tulemused graafiliselt, selleks kasuta nn. ASCII graafikat (https://en.wikipedia.org/wiki/ASCII_art):
imiteeri tekstisümbolite abil täringu külje kujutist. Täiendamiseks:

Kasutaja võib alguses ise valida, mitu korda täringut visata.
Mängida võib mitu inimest, programmi alguses küsitakse inimeste nimesid.
Täringut imiteeritakse kolmemõõtmelisena."""

import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    *    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  *      │",
        "│         │",
        "│      *  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  *      │",
        "│    *    │",
        "│      *  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  *   *  │",
        "│         │",
        "│  *   *  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  *   *  │",
        "│    *    │",
        "│  *   *  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  *   *  │",
        "│  *   *  │",
        "│  *   *  │",
        "└─────────┘",
    ),
}

def print_dice(value):
    for line in DICE_ART[value]:
        print(line)

def main():
    names_input = input("Hello! Write players names (use comma): ")
    players = [name.strip() for name in names_input.split(",")]

    throws = int(input("How many times should the dice be rolled? "))

    print("\n Game starts!\n")

    for t in range(1, throws + 1):
        print(f" ROUND {t}")
        for player in players:
            roll = random.randint(1, 6)
            print(f"\n{player} rolls: {roll}")
            print_dice(roll)
        print("\n" + "-" * 12 + "\n")

if __name__ == "__main__":
    main()
