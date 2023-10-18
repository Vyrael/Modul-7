from faker import Faker
fake = Faker()

class bussiness_card:
    def __init__(self, name, surname, company_name, position, email):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self.email = email

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'

def person():
    fake_name = fake.name()
    fake_company_name = fake.company()
    fake_position = fake.job()
    fake_email= fake.email()
    fake_person = bussiness_card(name=fake_name, surname="", company_name=fake_company_name, position=fake_position, email=fake_email)
    return fake_person

bussiness_cards = [for i in range(5):
    print(person())]




