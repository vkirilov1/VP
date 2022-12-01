import random


class Animal:
    def __init__(self, name, years, food_type):
        self.name = name
        self.years = years
        self.food_type = food_type

        def make_sound():
            pass

        def eat_food():
            pass


class Cat(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self):
        print("Meow!")

    def eat_food(self, food_count):
        if food_count >= 10:
            food_count -= 10
            return food_count
        elif food_count <= 0:
            self.make_sound()
            self.make_sound()
            return 0


class Dog(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self):
        print("Bark!")

    def eat_food(self, food_count, eat_quantity=5):
        if food_count <= 0:
            food_count = 0
            return food_count
        else:
            food_count -= eat_quantity
            return food_count


class Duck(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self):
        print("Quack!")

    def eat_food(self, food_count):
        random_food = random.randint(1, 9)
        if food_count <= 0:
            food_count -= random_food
            return food_count
        else:
            self.make_sound()
            food_count -= random_food
            return food_count


class Horse(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self):
        print("Snort!")

    def eat_food(self, food_count):
        if food_count >= 15:
            food_count -= 15
            return food_count
        elif 15 >= food_count > 0:
            food_count -= 8
            return food_count
        else:
            food_count = 0
            return food_count


animals_list = []
food_dict = {"fish":200, "dog_food":100, "fish_food":80, "horse_food":120}

cat1 = Cat("Elizabeth", 2, "fish")
cat2 = Cat("Ivan", 5, "fish")
cat3 = Cat("Gosho", 4, "fish")
dog1 = Dog("Tita", 5, "dog_food")
dog2 = Dog("Petko", 8, "dog_food")
duck1 = Duck("Dani", 2, "fish_food")
duck2 = Duck("Luyben", 1, "fish_food")
duck3 = Duck("Petur", 2, "fish_food")
horse1 = Horse("Veni", 7, "horse_food")
horse2 = Horse("Evtimii", 5, "horse_food")

animals_list.append(cat1)
animals_list.append(cat2)
animals_list.append(cat3)
animals_list.append(dog1)
animals_list.append(dog2)
animals_list.append(duck1)
animals_list.append(duck2)
animals_list.append(duck3)
animals_list.append(horse1)
animals_list.append(horse2)

for i in range(10):
    print("======")
    for n in animals_list:
        food_dict[n.food_type] = n.eat_food(food_dict[n.food_type])
        if food_dict[n.food_type] <= 0:
            print(f"{n.name} the {n.__class__.__name__} just ate 0 {n.food_type}, there's 0 left.")
        else:
            print(f"{n.name} the {n.__class__.__name__} just ate {food_dict[n.food_type] - n.eat_food(food_dict[n.food_type])} {n.food_type}, there's {food_dict[n.food_type]} left. ")
