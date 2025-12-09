"""Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab
ekraanile nimelise tervituse koos tekstiga, mis ütleb, kas tegemist on 7-18-aastase inimesega."""

def greet_by_name(name: str) -> str:
    return f"Hello, {name}!"
def verify_age(age: int) -> str:
    if 7 <= age <= 18:
        return "You are between 7 and 18 years old."
    else:
        return "You are not between 7 and 18 years old."


if __name__ == '__main__':
    name = input("Sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus: "))
    greeting = greet_by_name(name)
    age_text = verify_age(age)
    print(greeting)
    print(age_text)

