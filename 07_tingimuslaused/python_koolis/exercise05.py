"""Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja väljastab tulemuse Fahrenheiti kraadides.
Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui teistpidi? Proovi."""

celsius = float(input("Sisestage temperatuur Celsiuse kraadides:"))
fahrenheit = float(input("Sisetage temperatuur Fahrenheit kraadides:"))
print(f"{celsius}°C on {fahrenheit}°F")

scale = input("Kas sisestatud temperatuur on Celsiuse (C) või Fahrenheiti (F) kraadides? ").upper()

if scale == "C":
    celsius = float(input("Sisestage temperatuur Celsiuse kraadides: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C on {fahrenheit}°F")
elif scale == "F":
    fahrenheit = float(input("Sisestage temperatuur Fahrenheiti kraadides: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F on {celsius}°C")
else:
    print("Viga! Palun sisestage C või F")

if "__main__" == '__name__':
 celsius = float(input("Sisestage temperatuur Celsiuse kraadides:"))
fahrenheit = float(input("Sisetage temperatuur Fahrenheit kraadides:"))
print(f"{celsius}°C on {fahrenheit}°F")
