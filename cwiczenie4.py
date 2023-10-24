from faker import Faker
from datetime import datetime
fake = Faker()

class BaseContact:
    
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        
    @property
    def name_length(self):
        return len(self.name) + len(self.surname) 
    
    def __str__(self):
        return f'{self.name} {self.surname} {self.phone_number} {self.email}' 
        
    def contact(self):
        return f"Wybieram numer {self.phone_number} i dzwonię do {self.name} {self.surname}"
    
    
class BussinessContact(BaseContact):
    
    def __init__(self,position,company_name,bussiness_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.bussiness_number = bussiness_number
        
    
    def __str__(self):
        return f'{self.name} {self.surname} {self.phone_number} {self.email} {self.position} {self.company_name} {self.bussiness_number}' 
    
    def contact(self):
        return f"Wybieram numer {self.bussiness_number} i dzwonię do {self.name} {self.surname}"

def create_contacts(type,amount):
    contact_list = []
    if type == "base":
        for i in range(amount):
            fake_name_surname = fake.name() #new
            fake_name_surname = fake_name_surname.split(" ")#new
            fake_name = fake_name_surname[0]#new
            fake_surname = fake_name_surname[1]#new
            fake_phone_number = fake.phone_number()
            fake_email= fake.email()
            fake_person = BaseContact(name=fake_name, surname=fake_surname, phone_number=fake_phone_number, email=fake_email)
            contact_list.append(fake_person)
        return contact_list
    elif type == "bussiness":
        for i in range(amount):
            fake_name_surname = fake.name() #new
            fake_name_surname = fake_name_surname.split(" ")#new
            fake_name = fake_name_surname[0]#new
            fake_surname = fake_name_surname[1]#new
            fake_phone_number = fake.phone_number()
            fake_email= fake.email()
            fake_position = fake.job()
            fake_company = fake.company()
            fake_bussiness_number = fake.phone_number()
            fake_person = BussinessContact(name=fake_name, surname=fake_surname, phone_number=fake_phone_number, email=fake_email, position=fake_position,company_name=fake_company, bussiness_number=fake_bussiness_number)
            contact_list.append(fake_person)
        return contact_list
    else:
        print("wrong type. try base or bussiness")
        
fake_basic_contacts = create_contacts("base",2)
fake_bussiness_contacts = create_contacts("bussiness",2)
print(fake_basic_contacts[0])
print(fake_bussiness_contacts[0])
print(fake_basic_contacts[0].contact())
print(fake_bussiness_contacts[0].contact())
print("---------------------------------------------------------------------------------------------")
print(fake_basic_contacts[0].name_length)
print(fake_bussiness_contacts[0].name_length)

print("-----------------------------------------------------------------------")

def measure_time(func):
    def wrapper():
        start_time = datetime.now()
        result = func()
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time}")
        return result
    return wrapper

@measure_time
def generate_contacts():
    fake_contacts = create_contacts("base", 1000)
    return fake_contacts

fake_basic_contacts = generate_contacts()