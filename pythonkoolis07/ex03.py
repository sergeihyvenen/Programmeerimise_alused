"""
Tee programm, mis väljastab failist luuletus.txt kasutaja poolt soovitud rea nt:

Mitmendat rida soovid kuvada:
>> 7
Error tuleb ette siis,
NB! Faili avamiseks ja rea väljastamiseks koosta eraldi alamprogramm (ehk funktsioon).
"""

from ex02 import *

def print_line_from_file(lineNumber: int, filename: str) -> None:
    message = ""
    with open(filename, encoding="utf-8") as f:
        for index, line in enumerate(f):
            if (index + 1) == lineNumber:
                print(message + line)
                break
        else:
            print("Viga! Luuletusele ei ole nii palju ridu.")



if __name__ == "__main__":
    file_name = "luuletus.txt"
    user_input = input("Mitmedat rida soovid kuvada:")
    if user_input.isdigit():
        print_line_from_file(int(user_input), file_name)
    else:
        print("Viga! Sisesta positiivne täisarv!")