class Vehicle:
    def __init__(self, brand, model, engine_size, max_speed, kilometers_traveled, capacity):
        self.brand = brand
        self.model = model
        self.engine_size = engine_size
        self.max_speed = max_speed
        self.kilometers_traveled = kilometers_traveled
        self.capacity = capacity

    def print_info(self):
        print(f"Vehicle({self.brand}, {self.model}, {self.engine_size}, {self.max_speed}, {self.kilometers_traveled}, {self.capacity})")


class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_size, max_speed, kilometers_traveled, price, bin, capacity=2):
        super().__init__(brand, model, engine_size, max_speed, kilometers_traveled, capacity)
        self.price = price
        self.bin = bin


class Car(Vehicle):
    def __init__(self, brand, model, engine_size, max_speed, kilometers_traveled, category, fuel_type, capacity=4):
        super().__init__(brand, model, engine_size, max_speed, kilometers_traveled, capacity)
        self.category = category
        self.fuel_type = fuel_type


class Bus(Vehicle):
    def __init__(self, brand, model, engine_size, max_speed, kilometers_traveled, capacity, firm, production_year):
        super().__init__(brand, model, engine_size, max_speed, kilometers_traveled, capacity)
        self.firm = firm
        self.production_year = production_year


vehicles_list = []
motorbike1 = Motorbike("Suzuki", "a", 4, 200, 15000, 50000, True)
motorbike2 = Motorbike("BMW", "b", 6, 220, 10000, 70000, False)
motorbike3 = Motorbike("Mercedes", "c", 6, 230, 60000, 2000, False)
car1 = Car("Mazda", "6", 60, 240, 90000, "Mazda", "Diesel")
car2 = Car("Mazda", "3", 50, 200, 10000, "Mazda", "Diesel")
car3 = Car("Mercedes", "c220", 65, 260, 100000, "Mercedes", "Diesel")
bus1 = Bus("Audi", "bus5000", 90, 180, 100000, 25, "Toshko OOD", 2010)
bus2 = Bus("BMW", "bus6000", 70, 200, 100800, 25, "Toshko OOD", 2010)
bus3 = Bus("Alfa Umrelo", "bus1000", 60, 210, 100100, 30, "Toshko OOD", 2012)
bus4 = Bus("Peugeot", "bus4000", 50, 220, 106000, 15, "Toshko OOD", 2016)

vehicles_list.append(motorbike1)
vehicles_list.append(motorbike2)
vehicles_list.append(motorbike3)
vehicles_list.append(car1)
vehicles_list.append(car2)
vehicles_list.append(car3)
vehicles_list.append(bus1)
vehicles_list.append(bus2)
vehicles_list.append(bus3)
vehicles_list.append(bus4)

print(vehicles_list)