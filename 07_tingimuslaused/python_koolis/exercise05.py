"""Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja väljastab tulemuse Fahrenheiti kraadides.
Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui teistpidi? Proovi."""

def convert_to_fahrenheit(celsius: float) -> float:
    return celsius * 1.8 + 32

def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) / 1.8

if __name__ == '__main__':
    while True:
        scale = input("Kas sisestate temperatuuri Celsiuse (C) või Fahrenheiti (F) kraadides? ").strip().upper()
        if scale == "C":
            celsius = float(input("Sisesta temperatuur Celsiuse kraadides: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C on {fahrenheit:.2f}°F")
        elif scale == "F":
            fahrenheit = float(input("Sisesta temperatuur Fahrenheiti kraadides: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F on {celsius:.2f}°C")
        else:
            print("Viga! Palun sisesta C või F.")
            continue
        again = input("Kas soovid veel teisendada? (jah/ei): ").strip().lower()
        if again != "jah":
            print("Programm lõpetas töö.")
            break
