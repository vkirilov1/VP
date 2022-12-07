import random


class InvalidParameterError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid class parameter: {self.name}, for name'


class InvalidAgeError(InvalidParameterError):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def __str__(self):
        return f'Invalid parameter: {self.age}, for age'


class InvalidSoundError(InvalidParameterError):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def __str__(self):
        return f'Invalid parameter: {self.sound}, for sound'


class JungleAnimal:
    def __init__(self, name, age, sound):
        try:
            self.name = name
            self.age = age
            self.sound = sound

            def print_animal():
                pass

            def daily_task():
                pass

            if type(name) != str:
                raise InvalidParameterError(self.name)

            if type(age) != int:
                raise InvalidAgeError(self.name, self.age)

            if type(sound) != str:
                raise InvalidSoundError(self.name, self.sound)

        except InvalidSoundError as error:
            self.has_error = True
            print(error)

        except InvalidAgeError as error:
            self.has_error = True
            print(error)

        except InvalidParameterError as error:
            self.has_error = True
            print(error)

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound, has_error=False):
        super().__init__(name, age, sound)
        self.has_error = False
        try:
            if age > 15:
                raise InvalidAgeError(self.name, self.age)

            r_count = 0
            for char in self.sound:
                if char == "r":
                    r_count += 1

            if r_count < 2:
                raise InvalidSoundError(self.name, self.sound)

        except InvalidAgeError as error:
            self.has_error = True
            print(error)

        except InvalidSoundError as error:
            self.has_error = True
            print(error)

    def print_animal(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals_list):
        for z in range(0, len(animals_list)):
            if animals_list[z].__class__.__name__ == "Human" or animals_list[z].__class__.__name__ == "Lemur":
                print(f"{self.name} the Jaguar hunted down {animals_list[z].name} the {animals_list[z].__class__.__name__}")
                animals_list.pop(z)
                break


class Lemur(JungleAnimal):
    def __init__(self, name, age, sound, has_error=False):
        super().__init__(name, age, sound)
        self.has_error = False

        try:
            if age > 10:
                raise InvalidAgeError(self.name, self.age)

            e_count = 0
            for char in self.sound:
                if char == "e":
                    e_count += 1

            if e_count < 1:
                raise InvalidSoundError(self.name, self.sound)

        except InvalidAgeError as error:
            self.has_error = True
            print(error)

        except InvalidSoundError as error:
            self.has_error = True
            print(error)

    def print_animal(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_task(self, count):
        if count >= 10:
            count -= 10
            print(f"{self.name} the ate a full meal of 10 fruits")
            return count
        elif 0 < count < 10:
            print(f"{self.name} the Lemur could only find {count} fruits")
            count = 0
            return count
        elif count <= 0:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0


class Human(JungleAnimal):
    def __init__(self, name, age, sound, has_error=False):
        super().__init__(name, age, sound)
        self.has_error = False

        try:
            if age > 10:
                raise InvalidAgeError(self.name, self.age)

            e_count = 0
            for char in self.sound:
                if char == "e":
                    e_count += 1

            if e_count < 1:
                raise InvalidSoundError(self.name, self.sound)

        except InvalidAgeError as error:
            self.has_error = True
            print(error)

        except InvalidSoundError as error:
            self.has_error = True
            print(error)

    def print_animal(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals_list, buildings_list):
        for i in range(0, len(animals_list)-1):
            if animals_list[i].name == self.name:

                if i == 0:
                    if animals_list[i+1].__class__.__name__ == "Human":
                        new_building = Building("building1")
                        buildings_list.append(new_building)

                elif i == len(animals_list):
                    if animals_list[i-1].__class__.__name__ == "Human":
                        new_building = Building("building2")
                        buildings_list.append(new_building)

                elif animals_list[i-1].__class__.__name__ == "Human" and animals_list[i+1].__class__.__name__ == "Human":
                    new_building = Building("building")
                    buildings_list.append(new_building)


class Building:
    def __init__(self, type):
        self.type = type


fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    number = random.randint(0, 9)

    if 0 <= number <= 3:
        animal = Lemur(names[random.randint(0, len(names)-1)], random.randint(7, 20), sounds[random.randint(0, len(sounds)-1)])
        if animal.has_error:
            continue
        animals.append(animal)

    elif 4 <= number <= 7:
        animal = Jaguar(names[random.randint(0, len(names)-1)], random.randint(7, 20), sounds[random.randint(0, len(sounds)-1)])
        if animal.has_error:
            continue
        animals.append(animal)

    elif 8 <= number <= 9:
        animal = Human(names[random.randint(0, len(names)-1)], random.randint(7, 20), sounds[random.randint(0, len(sounds)-1)])
        if animal.has_error:
            continue
        animals.append(animal)


print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if anim.__class__.__name__ == "Jaguar":
        anim.daily_task(animals)
    elif anim.__class__.__name__ == "Lemur":
        fruits = anim.daily_task(fruits)
    elif anim.__class__.__name__ == "Human":
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)