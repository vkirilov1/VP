class Account:
    def __init__(self, currency, acc_type, IBAN, balance=0):
        self.balance = balance
        self.currency = currency
        self.acc_type = acc_type
        self.IBAN = IBAN

    def print_account(self):
        return f" Account({self.balance}, {self.currency}, {self.acc_type}, {self.IBAN})"