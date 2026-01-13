"""Kt 7
1.Küsi kasutajalt 1 arv mille paned astmele 2,3,4 ja 5 kasutades kordust ning kuva tulemused ekraanile.
2.Peale seda küsi kasutajalt kas ta soovib teise arvuga seda teha või lõpetada. (Kordus)"""

def calculate_powers():
    while True:
           number = float(input("Enter a number:"))
           power = 2
           while power <= 5:
            print(f"{number} to the power of {power} = {number ** power}")
            power += 1
           answer = input("Do you want to try another number? (yes/no): ").lower()
           if answer != "yes":
            print("Program finished.")
            break
if __name__ == "__main__":
    calculate_powers()