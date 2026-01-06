"""Koosta programm, mis aitab lastel treenida liitmist.
 Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust. Kui vastus on õige, kiitma kasutajat, kui aga vale, andma õige vastuse ja esitama uue tehte. Järjest esitatavate tehete hulk võib olla programmis ette antud (näiteks 10), samuti võib olla ette antud piirid, kui suuri arve kasutajalt küsitakse (näiteks 1 kuni 50). Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast viimast tehet tulemuse. Näiteks:

Tere! Õpime arvutama. Esitan 10 liitmistehet, püüa vastata õigesti.
5 + 16 =
>> 21
Tubli, õige vastus!
18 + 23 =
>> 39
Sinu vastus polnud õige. Õige vastus on 41.
[...]
2 + 5 =
>> 7
Tubli, õige vastus!
See oli viimane ülesanne. Kogusid 10-st punktist 7.
Täiendusi vabal valikul:

Programm lubab kasutajal alguses sisestada, mitut tehet soovitakse.
Esitatavate arvude piirid saab kasutaja ette
anda (maksimum või nii miinimum kui maksimum).
Küsitakse mitte ainult liitmistehteid, vaid ka teisi (lahutamine, korrutamine, jagamine).
Vastavalt lõpptulemusele reageeritakse erinevalt:
"Ülihea!", "Olid tubli!", "Korralik keskmine tulemus!", "Püüad järgmisel korral rohkem." vms."""
import random

def math_test():
    print("Tere! Õpime arvutama.")
    while True:
        try:
            num_questions = int(input("Mitu ülesannet soovid lahendada? "))
            if num_questions <= 0:
                print("Palun sisesta positiivne arv.")
                continue
            break
        except ValueError:
            print("Palun sisesta korrektne number.")
    while True:
        try:
            min_num = int(input("Sisesta miinimumarv: "))
            max_num = int(input("Sisesta maksimumarv: "))
            if min_num > max_num:
                print("Miinimum ei saa olla suurem kui maksimum.")
                continue
            break
        except ValueError:
            print("Palun sisesta korrektne number.")
    correct_count = 0
    for i in range(1, num_questions + 1):
        a = random.randint(min_num, max_num)
        b = random.randint(min_num, max_num)
        correct_answer = a + b
        while True:
            try:
                user_answer = int(input(f"{i}. {a} + {b} = "))
                break
            except ValueError:
                print("Palun sisesta arvuline vastus.")
        if user_answer == correct_answer:
            print("Tubli, õige vastus!\n")
            correct_count += 1
        else:
            print(f"Sinu vastus polnud õige. Õige vastus on {correct_answer}.\n")
    print(f"See oli viimane ülesanne. Kogusid {num_questions}-st punktist {correct_count}.")
    score_percentage = correct_count / num_questions * 100
    if score_percentage == 100:
        print("Ülihea!")
    elif score_percentage >= 70:
        print("Olid tubli!")
    elif score_percentage >= 40:
        print("Korralik keskmine tulemus!")
    else:
        print("Püüad järgmisel korral rohkem.")

if __name__ == "__main__":
    math_test()
