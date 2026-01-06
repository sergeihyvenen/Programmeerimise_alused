"""Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt 5 korda ja lisab ka tervituse järjekorranumber."""

if __name__ == '__main__':
    name = input("Palun sisesta oma nimi:\n>> ")
    for i in range(1, 6):
        print(f"Ole tervitatud, {name}, {i}. korda.")