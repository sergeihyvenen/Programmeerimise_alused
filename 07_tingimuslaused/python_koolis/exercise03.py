"""Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos vastusega. Näiteks:

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5"""

def input_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Viga! Sisetage õige arv!")

def input_operator(prompt):
    while True:
        op = input(prompt)
        if op in ["+", "-", "*", "/"]:
            return op
        else:
            print("Viga! Sisetage korrektne tehe (+, -, *, /)!")

if __name__ == '__main__':
    a = input_number("Sisestage esimene arv: ")
    b = input_number("Sisestage teine arv: ")
    op = input_operator("Sisestage tehe (+, -, *, /): ")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b != 0:
            result = a / b
        else:
            result = "Viga! Nulliga ei saa jagada!"

    if isinstance(result, (int, float)):
        print(f"Tulemus: {a}{op}{b}={result}")
    else:
        print(result)


    if __name__ == '__main__':
        a = float(input("Sisestage esimene arv: "))
        b = float(input("Sisestage teine arv: "))
        op = input("Sisestage tehe (+, -, *, /): ")
        print(f"Tulemus: {a}{op}{b}={result}")

