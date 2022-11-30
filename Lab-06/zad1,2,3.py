class Person:
    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def print_person(self):
        print(self.first_name)
        print(self.last_name)
        print(self.nationality)


class Student(Person):
    def __init__(self, first_name, last_name, age, nationality,  university, yearsofgraduation):
        super().__init__(first_name, last_name, age, nationality)
        self.university = university
        self.yearsofgraduation = yearsofgraduation

    def print_student(self):
        print(f"Name: {self.first_name} {self.last_name} \n"
              f"Age: {self.age} \n"
              f"Nationality: {self.nationality} \n" 
              f"University: {self.university} \n"
              f"Year of graduation: {self.yearsofgraduation}")

class Lecturer(Person):
    def __init__(self, first_name, last_name, age, nationality, university, experience):
        super().__init__(first_name, last_name, age, nationality)
        self.university = university
        self.experience = experience

    def print_lecturer(self):
        print(f"Lecturer's university: {self.university} \n"
              f"Lecturer's experience in years: {self.experience}")

lecturers = []
students = []

alex = Student("Alex", "Petkov", 30, "Gypsy", "TU", 2025)
dimitur = Student("Dimitar", "Dimitrov", 15, "Bulgarian", "UNSS", 2024)
aleksei = Student("Aleksei", "Ivanov", 20, "Romanian", "NBU", 2025)

ivana = Lecturer("Ivana", "Ivanova", 50, "bulgarian", "TU", 15)
dragana = Lecturer("Dragana", "Petkova", 40, "bulgarian", "UNSS", 6)

lecturers.append(ivana)
lecturers.append(dragana)

students.append(alex)
students.append(dimitur)
students.append(aleksei)

print("Students information:\n")
for a in students:
    a.print_student()
    print("")

print("Lecturers information:\n")
for a in lecturers:
    a.print_lecturer()
    print("")
