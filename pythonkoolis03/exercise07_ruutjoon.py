"""Koosta programm, mis küsib kasutajalt arvu N ja väljastab
O-tähtedest koosneva ruudu suuruses NxN. Seejärel muutke programmi nii,
et ruudu diagonaalidel olevad märgid oleksid X-d, näiteks:

X O O O O O O O X
O X O O O O O X O
O O X O O O X O O
O O O X O X O O O
O O O O X O O O O
O O O X O X O O O
O O X O O O X O O
O X O O O O O X O
X O O O O O O O X
... või (paarisarvulise N-i puhul):

X O O O O O O O O X
O X O O O O O O X O
O O X O O O O X O O
O O O X O O X O O O
O O O O X X O O O O
O O O O X X O O O O
O O O X O O X O O O
O O X O O O O X O O
O X O O O O O O X O
X O O O O O O O O X
Tühikuid võid lisada vastavalt oma soovile."""

def joonista_ruut():
    N = int(input("Sisesta ruudu suurus N: "))

    ruut = "\n".join(
        " ".join(
            "X" if i == j or i + j == N - 1 else "O"
            for j in range(N)
        )
        for i in range(N)
    )

    print(ruut)
if __name__ == "__main__":
    joonista_ruut()