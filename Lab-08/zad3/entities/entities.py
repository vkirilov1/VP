class Item:
    def __init__(self, name):
        self.name = name
        self.durability = 100

    def print_item(self):
        return f"Item({self.name}|{self.durability})"


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.durability = 100
        self.damage = damage

    def print_item(self):
        return f"Weapon({self.name}|{self.damage}|{self.durability})"


class Character:
    def __init__(self, name, gender, playing_class, weapon=None, item=None):
        self.name = name
        self.gender = gender
        self.playing_class = playing_class
        self.weapon = weapon
        self.item = item

    def print_character(self):
        if self.weapon is None and self.item is None:
            return f"Character({self.name}, {self.gender}, {self.playing_class}, No weapon, No item)"
        elif self.weapon is not None and self.item is None:
            return f"Character({self.name}, {self.gender}, {self.playing_class}, {self.weapon.print_item()}, No item)"
        elif self.weapon is None and self.item is not None:
            return f"Character({self.name}, {self.gender}, {self.playing_class}, No weapon, {self.item.print_item()})"
        else:
            return f"Character({self.name}, {self.gender}, {self.playing_class}, {self.weapon.print_item()}, {self.item.print_item()})"
