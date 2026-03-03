"""
Palindroomiks nimetatakse sõna (ka sõnaühendit), mis on nii vasakult paremale kui paremalt vasakule lugedes täpselt ühesugunem (näit. "kook", "kuulilennuteetunneliluuk" jne).
Loo programm, mis trükib ekraanile välja kõik tekstifailis olevad sõnad, mis on palindroomid.
Alustekstiks võid kasutada suvalist teksti, kuid katsetada tasuks ka sõnaloenditega,
kus iga sõna asub eraldi real (näit. eesti keele sõnade algvormid e. lemmad veebilehelt http://www.eki.ee/tarkvara/wordlist/).
"""
import doctest

def is_palindrome(word: str) -> bool:
    return word == word[::-1]

def check_file_for_palindromes(filename: str) -> None:
    with open(filename, encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if len(word) > 1 and is_palindrome(word):
                print(word)

if __name__ == '__main__':
    filename = "lemmad2013.txt"
    print(f"failis {filename} esinevad järgmised palindroomid:")
    check_file_for_palindromes(filename)