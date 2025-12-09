"""Eelmise ülesande alusel koostage programm M-Koer (Matemaatiline Koer), millele antakse samuti ette kaks arvu ja tehtemärk, kuid vastus ei kirjutata mitte arvulisel kujul, vaid esitatakse "haukudes". Igaks juhuks: tsükleid pole vaja kasutada, me pole neid veel õppinud.

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: auh auh auh auh auh"""

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
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
        haukude_arv = int(result) if result > 0 else 0
        print("Tulemus:", "auh " * haukude_arv)
    else:
        print(result)