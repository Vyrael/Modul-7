class card:
    def __init__(self, name, surname, company_name, position, email):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self.email = email

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'

neo = card(name="Keanu", surname="Reeves", company_name="Matrix1", position="actor", email="neo@matrix.com")
trinity = card(name="CarryAnn", surname="Moss", company_name="Matrix2", position="actress", email="trinity@matrix.com")
director = card(name="Larry", surname="Wachowsky", company_name="Universal1", position="Director", email="l.wachowsky@matrix.com")
music = card(name="Don", surname="Davies", company_name="Universal2", position="MusicBy", email="don.d@matrix.com")
producer = card(name="Joel", surname="Silver", company_name="Universal3", position="Producer", email="j.silver@matrix.com")

wizytowki_matrix = [neo, trinity, director, music, producer]

for i in wizytowki_matrix:
    print(i)








