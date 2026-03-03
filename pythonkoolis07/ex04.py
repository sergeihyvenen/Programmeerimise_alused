"""
Koosta programm, mis küsib kasutajalt rea,
mille järele ta soovib failis luuletus.txt uut rida lisada ning seejärel lisab kasutaja poolt sisestatud rea nt:

Sisesta rida, mille järele soovid uut rida lisada:
>> Padja, teki viskan maha,
Sisesta rida, mida soovid lisada:
>> üles ärgata ma ei taha,
Tulemus failis luuletus.txt:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
üles ärgata ma ei taha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
"""
from ex02 import poem_list

def write_poem_file(poem_name: str, poem: list) -> None:
    with open(poem_name, "w", encoding="utf-8") as file:
        for line in poem:
            file.write(line + "\n")


def add_line_after(filename: str, target_line: str, new_line: str) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    found = False
    updated_lines = []

    for line in lines:
        updated_lines.append(line)
        if line.strip() == target_line.strip() and not found:
            updated_lines.append(new_line.strip() + "\n")
            found = True

    if not found:
        print("Viga! Sellist rida ei leitud failis.")
        return

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(updated_lines)

    print("Rida lisatud edukalt!")


if __name__ == "__main__":
    file_name = "luuletus.txt"

    write_poem_file(file_name, poem_list)

    target = input("Sisesta rida, mille järele soovid uut rida lisada:\n>> ")
    new_text = input("Sisesta rida, mida soovid lisada:\n>> ")

    add_line_after(file_name, target, new_text)

    with open(file_name, "r", encoding="utf-8") as file:
        print("\nFaili uus sisu:\n")
        print(file.read())