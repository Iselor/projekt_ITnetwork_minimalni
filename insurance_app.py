class InsuranceApp:
    def __init__(self):
        self.insured_persons = []

    def add_insured_person(self, person):
        self.insured_persons.append(person)

    def get_all_insured_persons(self):
        for person in self.insured_persons:
            print(person)

    def find_insured_person(self, name, surname):
        for person in self.insured_persons:
            if person.name == name and person.surname == surname:
                return person
        return None
