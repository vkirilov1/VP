import entities
import errors


class Menu:

    def print_menu(self):
        print("1. Create a new character\n"
              "2. Create a new weapon\n"
              "3. Create a new item \n"
              "4. Print all characters\n"
              "5. Delete an existing character\n"
              "6. Exit")

    def command_create_character(self, name, sex, ch_class):
        character = entities.Character(name, sex, ch_class)
        return character

    def run(self):
        characters = []
        while True:
            Menu.print_menu(self)

            choice = input("Choose an item from the menu: \n>")

            try:
                if choice == "1":
                    name = input("Enter name (must be at least 4 letters): ")
                    if len(name) < 4:
                        raise errors.InvalidDataFormat("Error! Name must be at least 4 letters long!")
                    for ch in characters:
                        if ch.name == name:
                            raise errors.CharacterExists("Error! Character's name is taken!")

                    sex = input("Enter character gender (must be at least 4 letters and can't contain numbers): ")
                    if len(sex) < 4:
                        raise errors.InvalidDataFormat("Error! Gender must be at least 4 letters long!")
                    elif any(char.isdigit() for char in sex):
                        raise errors.InvalidDataFormat("Error! Gender can't contain numbers!")

                    ch_class = input("Enter character class (must be Warrior, Mage, Priest, Rogue): ")
                    if ch_class != "Warrior" and ch_class != "Mage" and ch_class != "Priest" and ch_class != "Rogue":
                        raise errors.InvalidCharacterClass("Error! Character's class must be Warrior, Mage, Priest or Rogue!")

                    character = self.command_create_character(name, sex, ch_class)
                    characters.append(character)

                elif choice == "2":
                    name = input("Enter weapon name (must be at least 4 letters): ")
                    if len(name) < 4:
                        raise errors.InvalidDataFormat("Error! Name must be at least 4 letters long!")

                    damage = int(input("Enter weapon damage (must be positive number): "))
                    if 0 > damage:
                        raise errors.InvalidDataFormat("Error! Damage can't be below zero!")

                    ch_name = input("Enter the name of the character you want to equip this weapon to: ")

                    exists = False
                    for ch in characters:
                        if ch.name == ch_name:
                            ch.weapon = entities.Weapon(name, damage)
                            exists = True

                    if not exists:
                        raise errors.CharacterNotFound("Error! There is no such character!")

                elif choice == "3":
                    name = input("Enter item name (must be at least 4 letters): ")
                    if len(name) < 4:
                        raise errors.InvalidDataFormat("Error! Name must be at least 4 letters long!")

                    ch_name = input("Enter the name of the character you want to equip this item to: ")

                    exists = False
                    for ch in characters:
                        if ch.name == ch_name:
                            ch.item = entities.Item(name)
                            exists = True

                    if not exists:
                        raise errors.CharacterNotFound("Error! There is no such character!")

                elif choice == "4":
                    print("----------------------------")
                    print("Characters:")
                    for ch in characters:
                        print(ch.print_character())
                    print("----------------------------")

                elif choice == "5":
                    ch_name = input("Enter the name of the character you want to delete: ")

                    exists = False
                    for ch in characters:
                        if ch.name == ch_name:
                            characters.remove(ch)
                            exists = True

                    if not exists:
                        raise errors.CharacterNotFound("Error! There is no such character!")

                elif choice == "6":
                    break

                else:
                    raise errors.InvalidCommand("Error: Invalid choice")

            except Exception as error:
                print(f"{str(error)}")


if __name__ == '__main__':
    menu = Menu()
    menu.run()

