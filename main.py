from insurance_app import InsuranceApp
from insured_person import InsuredPerson

if __name__ == "__main__":
    app = InsuranceApp()

    while True:
        print("")
        print("1. Přidat pojištěného")
        print("2. Zobrazit seznam pojištěných")
        print("3. Vyhledat pojištěného")
        print("4. Ukončit aplikaci")
        print("")
        choice = input("Zvolte volbu: ")

        if choice == "1":
            name = input("Zadejte jméno: ")
            surname = input("Zadejte příjmení: ")
            age = int(input("Zadejte věk: "))
            phone = input("Zadejte telefonní číslo: ")
            person = InsuredPerson(name, surname, age, phone)
            app.add_insured_person(person)
        elif choice == "2":
            app.get_all_insured_persons()
        elif choice == "3":
            name = input("Zadejte jméno: ")
            surname = input("Zadejte příjmení: ")
            person = app.find_insured_person(name, surname)
            if person:
                print(person)
            else:
                print("Pojištěný nenalezen.")
        elif choice == "4":
            break
        else:
            print("Neplatná volba.")
