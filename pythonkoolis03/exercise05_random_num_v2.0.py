"""Täienda eelmist programmi selliselt, et kasutajal oleks arvu arvamiseks 5 korda, s. t. kui
viie korra jooksul ära ei arvata, ütleb arvuti, et kaotasid, ning
teatab õige arvu. Täienda vastavalt ka plokkskeemi."""

import random

def rand_num():
    right_num = random.randint(1, 20)
    attempts = 5

    print("Mõtlesin ühele täisarvule 1–20ni. Mis see arv on?")
    print("Sul on ainult 5 katset!!!")

    while attempts > 0:
        num = int(input(">> "))
        if num == right_num:
            print("Tubli! Õige arv.")
            return
        elif num < right_num:
            print("Liiga väike arv. Proovi uuesti.")
        else:
            print("Liiga suur arv. Proovi uuesti.")
        attempts -= 1
        print("Katseid jäänud:", attempts)
    print("Kaotasid! Õige arv oli", right_num)
if __name__ == "__main__":
    rand_num()