class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def print_person(self):
        return f"Person({self.name}, {self.age}, {self.job})"


person1 = Person("Ivan", 15, "programmer")

my_file = open("info.txt", "w", encoding="utf-8")
my_file.writelines(person1.print_person())
my_file.close()


