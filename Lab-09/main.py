import entities
import errors
import random


class Menu:

    def print_menu(self):
        print("1. Create user\n"
              "2. Create a new acc for user\n"
              "3. Print all users\n"
              "4. Print user's accounts\n"
              "5. Deposit money\n"             
              "6. Withdraw money\n"
              "7. Exit")

    def command_create_user(self, name, EGN, accounts):
        return entities.User(name, EGN, accounts)

    def command_create_acc(self, currency, acc_type, IBAN):
        return entities.Account(currency, acc_type, IBAN)

    def run(self):

        users = []
        bank = entities.Bank(users)

        while True:
            Menu.print_menu(self)

            choice = input("Choose an option from the menu: \n>")

            try:
                if choice == "1":
                    name = input("Input user's name (must be at least 4 letters long): ")
                    if len(name) < 4:
                        raise errors.InvalidDataFormat("Error! Username must be at least 4 letters long!")
                    if any(char.isdigit() for char in name):
                        raise errors.InvalidDataFormat("Error! Username can't contain numbers!")

                    EGN = input("Input user's EGN (must be at least 10 numbers long): ")
                    if len(EGN) < 10:
                        raise errors.InvalidDataFormat("Error! EGN must be at least 10 numbers long!")
                    if any(char.isalpha() for char in EGN):
                        raise errors.InvalidDataFormat("Error! EGN can't contain letters!")

                    accounts = []
                    user = self.command_create_user(name, EGN, accounts)
                    bank.add_user(user)

                elif choice == "2":
                    currency = input("Enter currency(Must be BGN, EUR, USD or JPY): ")
                    if currency != "BGN" and currency != "EUR" and currency != "USD" and currency != "JPY":
                        raise errors.InvalidDataFormat("Error! Currency must be BGN, EUR, USD or JPY")

                    acc_type = input("Enter account type(Must be CURRENT, SAVINGS or CREDIT): ")
                    if acc_type != "CURRENT" and acc_type != "SAVINGS" and acc_type != "CREDIT":
                        raise errors.InvalidDataFormat("Error! Account type must be CURRENT, SAVINGS or CREDIT")

                    bonus = random.randint(1111111111, 9999999999)
                    IBAN = "BG9812" + str(bonus)

                    account = self.command_create_acc(currency, acc_type, IBAN)
                    username = input("Enter the username you want to add this account to: ")

                    exists = False
                    for us in bank.users:
                        if username == us.names:
                            us.accounts.append(account)
                            exists = True

                    if not exists:
                        raise errors.UserNotFound("Error! User doesn't exist!")

                elif choice == "3":
                    print("-------------------------")
                    print("Users:")
                    for us in bank.users:
                        print(us.print_user())
                    print("-------------------------")

                elif choice == "4":
                    username = input("Enter the username you want to see all accounts of: ")

                    exists = False
                    for us in bank.users:
                        if username == us.names:
                            exists = True
                            if len(us.accounts) == 0:
                                raise errors.InvalidDataFormat("Error! User doesn't have any accounts!")
                            for acc in us.accounts:
                                print(acc.print_account())

                    if not exists:
                        raise errors.UserNotFound("Error! User doesn't exist!")

                elif choice == "5":
                    deposit_money = int(input("Enter money to deposit: "))
                    if type(deposit_money) == str:
                        raise errors.InvalidDataFormat("Error! Money can't contain letters!")

                    username = input("Type the username you want to add the money to: ")

                    exists = False
                    acc_exists = False
                    for us in bank.users:
                        if username == us.names:
                            exists = True
                            account_info1 = input("Input account's type: ")
                            account_info2 = input("Input account's currency: ")
                            for acc in us.accounts:
                                if acc.acc_type == account_info1 and acc.currency == account_info2:
                                    acc_exists = True
                                    acc.balance += deposit_money

                    if not exists:
                        raise errors.UserNotFound("Error! User doesn't exist!")
                    if not acc_exists:
                        raise errors.AccNotFound("Error! User doesn't have such account!")

                elif choice == "6":
                    withdraw_money = int(input("Enter money to withdraw: "))
                    if type(withdraw_money) == str:
                        raise errors.InvalidDataFormat("Error! Money can't contain letters!")

                    username = input("Type the username you want to withdraw the money from: ")

                    exists = False
                    acc_exists = False
                    for us in bank.users:
                        if username == us.names:
                            exists = True
                            account_info1 = input("Input account's type: ")
                            account_info2 = input("Input account's currency: ")
                            for acc in us.accounts:
                                if acc.acc_type == account_info1 and acc.currency == account_info2:
                                    acc_exists = True
                                    if acc.balance < withdraw_money:
                                        raise errors.NotEnoughMoney("Error! Account doesn't have enough money!")
                                    acc.balance -= withdraw_money

                    if not exists:
                        raise errors.UserNotFound("Error! User doesn't exist!")
                    if not acc_exists:
                        raise errors.AccNotFound("Error! User doesn't have such account!")

                elif choice == "7":
                    break

                else:
                    raise errors.InvalidCommand("Invalid command type!")

            except Exception as error:
                print(f"{str(error)}")


if __name__ == '__main__':
    menu = Menu()
    menu.run()
