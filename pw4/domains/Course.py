class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.students = {}
        self.credit = credit