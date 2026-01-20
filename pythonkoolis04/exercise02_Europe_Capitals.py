""" Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).
Väljasta linnad eraldi ridadena.
Järjesta need tähestikulisse järjekorda.
Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna",
kus linnade arv leitakse vastava funktsiooni abil."""

capitals = ["Tallinn", "Riga", "Helsinki", "Rome", "Vilnius", "Berlin", "Paris", "Stockholm", "Warsaw", "Kiev"]

def print_list(elements: list) -> None:
    for element in elements:
        print(element, end= ", ")
    print()

def print_list_with_numbers(elements: list[str]) -> None:
    for i, element in enumerate(elements, start=1):
        print(f"{i}. {element}", end= ", ")


def sort_in_place(elements: list) -> None:
    elements.sort()

def add_capitals(capitals: list[str], amount: int) -> None:
    for i in range(amount):
        capitals.append(input(f"{i + 1}. Sisesta Euroopa pealinn:"))
def summarize(capitals: list[str]) -> None:
    print(f"In our list {len(capitals)} Europe capitals")

if __name__ == '__main__':
    print("Original:")
    print_list(capitals)
    sort_in_place(capitals)
    print("Sorted:")
    print_list(capitals)
    add_capitals(capitals, amount=2)
    sort_in_place(capitals)
    print_list_with_numbers(capitals)
    summarize(capitals)
