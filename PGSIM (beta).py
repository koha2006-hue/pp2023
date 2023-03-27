#create a public governmental services information management system (birth, marriage, death, divorce, etc.)
class citizen:
    def __init__(self, name, id, DoB, nationality, place_of_origin, place_of_residence, marriage, spouse):
        self.name = name
        self.id = id
        self.DoB = DoB
        self.nationality = nationality
        self.place_of_origin = place_of_origin
        self.place_of_residence = place_of_residence
        self.marriage = marriage
        self.spouse = spouse
class management:
    def __init__(self):
        self.citizen = {}
    def add_citizen(self):
        print ("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        citizen.DoB = input("Date of birth: ")
        citizen.nationality=("Nationality:")
        citizen.place_of_origin = input("Place of origin: ")
        citizen.place_of_residence = input("Place of residence: ")
        citizen.marriage = input("Marriage status: ")
        if citizen.marriage == "married":
            citizen.spouse = input("Spouse: ")
        else:
            citizen.spouse = "none"
        self.citizen[citizen.id] = citizen
    def add_marriage(self):
        husband=citizen()
        wife=citizen()
        print ("Enter the following information:")
        husband.name = input("Name of the first citizen: ")
        husband.id = input("ID of the first citizen: ")
        if husband.marriage == "married":
            print ("The first citizen is already married.")
            return
        wife.name = input("Name of the second citizen: ")
        wife.id = input("ID of the second citizen: ")
        if wife.marriage == "married":
            print ("The second citizen is already married.")
            return
        marriage_date = input("Date of marriage: ")
        marriage_place = input("Place of marriage: ")       
        marriage_certificate = input("Marriage certificate: ")
        self.marriage = {husband, wife, marriage_date, marriage_place, marriage_certificate}
        husband.marriage = "married"
        wife.marriage = "married"
        husband.spouse = wife.name
        wife.spouse = husband.name
        self.citizen[citizen.id] = citizen
    def add_divorce(self):
        husband=citizen()
        wife=citizen()
        print ("Enter the following information:")
        husband.name = input("Name of the first citizen: ")
        husband.id = input("ID of the first citizen: ")
        if husband.marriage == "single":
            print ("The first citizen is not married.")
            return
        wife.name = input("Name of the second citizen: ")
        wife.id = input("ID of the second citizen: ")
        if wife.marriage == "single":
            print ("The second citizen is not married.")
            return
        divorce_date = input("Date of divorce: ")
        divorce_place = input("Place of divorce: ")
        divorce_certificate = input("Divorce certificate: ")
        self.divorce = {husband, wife, divorce_date, divorce_place, divorce_certificate}
        husband.marriage = "single"
        wife.marriage = "single"
        husband.spouse = "none"
        wife.spouse = "none"
        self.citizen[citizen.id] = citizen
    def birth_declaration(self):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        citizen.DoB = input("Date of birth: ")
        citizen.Place_of_birth = input("Place of birth: ")
        self.father = input("Father's name: ")
        self.father_id = input("Father's ID: ")
        self.mother = input("Mother's name: ")
        self.mother_id = input("Mother's ID: ")
        self.birth_certificate = input("Birth certificate: ")
        self.birth = {citizen.name, citizen.id, citizen.DoB, citizen.Place_of_birth, self.father, self.father_id, self.mother, self.mother_id, self.birth_certificate}
        self.citizen[citizen.id] = citizen
    def death_declaration(self):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        citizen.DoB = input("Date of birth: ")
        citizen.place_of_origin = input("Place of origin: ")
        citizen.place_of_residence = input("Place of residence: ")
        self.reasion_of_death = input("Reason of death: ")
        self.date_of_death = input("Date of death: ")
        self.place_of_death = input("Place of death: ")
        self.death_certificate = input("Death certificate: ")
        self.death = {citizen.name, citizen.id, citizen.DoB, citizen.place_of_origin, citizen.place_of_residence, self.reasion_of_death, self.date_of_death, self.place_of_death, self.death_certificate}
        self.citizen[citizen.id] = citizen
    def change_name(self):
        self.search_citizen()
        self.new_name = input("New name: ")
        self.change_name_certificate = input("Change name certificate: ")
        self.change_name = {citizen.name, citizen.id, self.new_name, self.change_name_certificate}
        self.citizen[citizen.id] = citizen
    def print_citizen(self, citizen):
        print("Name: ", citizen.name)
        print("ID: ", citizen.id)
        print("Date of birth: ", citizen.DoB)
        print("Nationality: ", citizen.nationality)
        print("Place of origin: ", citizen.place_of_origin)
        print("Place of residence: ", citizen.place_of_residence)
        print("Marriage status: ", citizen.marriage)
        if citizen.marriage == "married":
            print("Spouse: ", citizen.spouse)
    def search_citizen(self):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        if self.citizen[citizen.id] == citizen:
            print("The citizen is found.")
            self.print_citizen(citizen)
        else:
            print("The citizen is not found.")
    def search_marriage(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.marriage == {self.husband, self.wife}:
            print("The marriage is found.")
        else:
            print("The marriage is not found.")
    def search_birth(self, citizen):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        if self.birth == {citizen.name, citizen.id}:
            print("The birth is found.")
        else:
            print("The birth is not found.")
    def search_death(self, citizen):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        if self.death == {citizen.name, citizen.id}:
            print("The death is found.")
        else:
            print("The death is not found.")
    def search_divorce(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.divorce == {self.husband, self.wife}:
            print("The divorce is found.")
        else:
            print("The divorce is not found.")
    def delete_citizen(self):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        if self.citizen[citizen.id] == citizen:
            del self.citizen[citizen.id]
            print("The citizen is deleted.")
        else:
            print("The citizen is not found.")
    def delete_marriage(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.marriage == {self.husband, self.wife}:
            del self.marriage
            print("The marriage is deleted.")
        else:
            print("The marriage is not found.")
    def delete_birth(self, citizen):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        if self.birth == {citizen.name, citizen.id}:
            del self.birth
            print("The birth is deleted.")
        else:
            print("The birth is not found.")
    def delete_death(self):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        if self.death == {citizen.name, citizen.id}:
            del self.death
            print("The death is deleted.")
        else:
            print("The death is not found.")
    def delete_divorce(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.divorce == {self.husband, self.wife}:
            del self.divorce
            print("The divorce is deleted.")
        else:
            print("The divorce is not found.")
    def update_citizen(self):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        if self.citizen[citizen.id] == citizen:
            citizen.name = input("Name: ")
            citizen.id = input("ID: ")
            citizen.DoB = input("Date of birth: ")
            citizen.place_of_origin = input("Place of origin: ")
            citizen.place_of_residence = input("Place of residence: ")
            self.citizen[citizen.id] = citizen
            print("The citizen is updated.")
        else:
            print("The citizen is not found.")
    def update_marriage(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.marriage == {self.husband, self.wife}:
            self.husband = input("Husband's name: ")
            self.husband_id = input("Husband's ID: ")
            self.wife = input("Wife's name: ")
            self.wife_id = input("Wife's ID: ")
            self.marriage = {self.husband, self.wife}
            print("The marriage is updated.")
        else:
            print("The marriage is not found.")
    def update_birth(self):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        if self.birth == {citizen.name, citizen.id}:
            citizen.name = input("Name: ")
            citizen.id = input("ID: ")
            citizen.DoB = input("Date of birth: ")
            citizen.place_of_origin = input("Place of origin: ")
            citizen.place_of_residence = input("Place of residence: ")
            self.birth = {citizen.name, citizen.id, citizen.DoB, citizen.place_of_origin, citizen.place_of_residence}
            print("The birth is updated.")
        else:
            print("The birth is not found.")
    def update_death(self):
        print("Enter the following information:")
        citizen.name = input("Name: ")
        citizen.id = input("ID: ")
        if self.death == {citizen.name, citizen.id}:
            citizen.name = input("Name: ")
            citizen.id = input("ID: ")
            citizen.DoB = input("Date of birth: ")
            citizen.place_of_origin = input("Place of origin: ")
            citizen.place_of_residence = input("Place of residence: ")
            self.death = {citizen.name, citizen.id, citizen.DoB, citizen.place_of_origin, citizen.place_of_residence}
            print("The death is updated.")
        else:
            print("The death is not found.")
    def update_divorce(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.divorce == {self.husband, self.wife}:
            self.husband = input("Husband's name: ")
            self.husband_id = input("Husband's ID: ")
            self.wife = input("Wife's name: ")
            self.wife_id = input("Wife's ID: ")
            self.divorce = {self.husband, self.wife}
            print("The divorce is updated.")
        else:
            print("The divorce is not found.")