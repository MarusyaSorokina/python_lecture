class Student:
    def __init__(self, name):
        self.name = name
        self.model = self.Notebook()

    def print_info(self):
        return f"{self.name} => {self.model}"

    class Notebook:

        def __str__(self):
            return f"{self.model_note}"

        @property
        def model_note(self):
            return "HP, i7, 16Gb"


stud = Student("Roman")
stud2 = Student("Vladimir")
print(stud.print_info())
print(stud2.print_info())
