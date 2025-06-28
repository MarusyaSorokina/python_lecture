from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, fio, old):
        self.fio = fio
        self.old = old

    @abstractmethod
    def print_info(self):
        pass


class Student(Human):
    def __init__(self, fio, old, groupe, score):
        super().__init__(fio, old)
        self.groupe = groupe
        self.score = score

    def info_stud(self):
        return f"{self.groupe} {self.score}"

    def print_info(self):
        print(f"Студент: {self.fio}, Возраст: {self.old}, Группа: {self.groupe}, Средний бал: {self.score}")


class Teacher(Human):
    def __init__(self, fio, old, discipline, rating):
        super().__init__(fio, old)
        self.discipline = discipline
        self.rating = rating

    def info_teacher(self):
        return f"{self.discipline} {self.rating}"

    def print_info(self):
        print(f"Преподаватель: {self.fio}, Возраст: {self.old}, Дисциплина: {self.discipline}, Рейтинг: {self.rating}")


class Graduate(Student):
    def __init__(self, fio, old, groupe, score, diploma):
        super().__init__(fio, old, groupe, score)
        self.diploma = diploma

    def info_grad(self):
        return f"{self.diploma}"

    def print_info(self):
        print(f"Дипломник: {self.fio}, Возраст: {self.old}, Группа: {self.groupe}, Средний бал: {self.score}, Тема "
              f"диплома: {self.diploma}")


st = [Student("Батодалаев Даши", 16, "ГК Web_011", 5),
      Student("Загидуллин Линар", 32, "РПО PD_011", 5),
      Graduate("Шугани Сергей", 15, "РПО PD_011", 5, "Защита персональных данных"),
      Teacher("Даньшин Андрей", 38, "Астрофизика", 110),
      Student("Маркин Даниил", 17, "ГК Python_011", 5),
      Teacher("Башкиров Алексей", 45, "Разработка приложений", 20)]

for elem in st:
    elem.print_info()


