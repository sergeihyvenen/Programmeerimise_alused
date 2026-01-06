import random

def math_quiz():
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
    math_quiz()
