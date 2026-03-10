"""
Koosta programm telefoniraamatu loomiseks.



1.Peab saama sisestada nime ja telefoni numbrit

2.Samal nimel võib olla ainult üks telefoni number

3.Peab saama küsida nime järgi numbrit ja numbri järgi nime

    a.Kui vastet pole, siis peab võimaldama lisamist

4.Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)

5.Lisa funktsioon terve raamatu kuvamiseks
"""

import os

FILE_NAME = "phonebook.txt"

def load_data():
    phonebook = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, number = line.strip().split(",")
                phonebook[name] = number
    return phonebook

def save_data(phonebook):
    with open(FILE_NAME, "w") as f:
        for name, number in phonebook.items():
            f.write(name + "," + number + "\n")

def add_contact(phonebook):
    name = input("Enter name: ")
    if name in phonebook:
        print("Name already exists")
        return
    number = input("Enter number: ")
    phonebook[name] = number
    save_data(phonebook)

def search_by_name(phonebook):
    name = input("Enter name: ")
    if name in phonebook:
        print("Number:", phonebook[name])
    else:
        print("Not found")
        choice = input("Add it? (y/n): ")
        if choice.lower() == "y":
            number = input("Enter number: ")
            phonebook[name] = number
            save_data(phonebook)

def search_by_number(phonebook):
    number = input("Enter number: ")
    for name, num in phonebook.items():
        if num == number:
            print("Name:", name)
            return
    print("Not found")
    choice = input("Add it? (y/n): ")
    if choice.lower() == "y":
        name = input("Enter name: ")
        phonebook[name] = number
        save_data(phonebook)

def show_all(phonebook):
    if not phonebook:
        print("Phonebook is empty")
    else:
        for name, number in phonebook.items():
            print(name, "-", number)

def menu():
    phonebook = load_data()
    while True:
        print("Phonebook by Sergei Hüvenen v1.0")
        print("\n1 Add contact")
        print("2 Search by name")
        print("3 Search by number")
        print("4 Show all")
        print("5 Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_by_name(phonebook)
        elif choice == "3":
            search_by_number(phonebook)
        elif choice == "4":
            show_all(phonebook)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()