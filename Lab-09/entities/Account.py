<<<<<<< HEAD
class Account:
    def __init__(self, currency, acc_type, IBAN, balance=0):
        self.balance = balance
        self.currency = currency
        self.acc_type = acc_type
        self.IBAN = IBAN

    def print_account(self):
=======
class Account:
    def __init__(self, currency, acc_type, IBAN, balance=0):
        self.balance = balance
        self.currency = currency
        self.acc_type = acc_type
        self.IBAN = IBAN

    def print_account(self):
>>>>>>> e75c3a72cc9faaba0c276e43501f5c8663310736
        return f" Account({self.balance}, {self.currency}, {self.acc_type}, {self.IBAN})"