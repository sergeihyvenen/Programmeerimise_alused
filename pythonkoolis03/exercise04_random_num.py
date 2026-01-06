"""Koosta mäng, kus saate ära arvata arvuti poolt mõeldud täisarvu ühest kahekümneni. nt:

Mõtlesin ühele täisarvule 1-20ni. Mis arv see on?
>> 15
Liiga suur, proovi uuesti.
>> 7
Liiga väike, proovi uuesti.
>> 9
Liiga väike, proovi uuesti.
>> 11
Tubli, arvasid ära. Arv oli 11.
Enne ülesande lahendamist mõelge välja mängu algoritm ja koostage selle kohta plokkskeem."""

import random

def rand_num():
    right_num = random.randint(1, 20)
    print("Mõtlesin ühele täisarvule 1–20ni. Mis see arv on?")

    while True:
        num = int(input(">> "))
        if num < right_num:
            print("Liiga väike arv. Proovi uuesti")
        elif num > right_num:
            print("Liiga suur arv. Proovi uuesti")
        else:
            print("Tubli! Õige arv.")
            break
if __name__ == "__main__":
    rand_num()
