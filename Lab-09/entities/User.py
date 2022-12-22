class User:
    def __init__(self, names, EGN, accounts):
        self.names = names
        self.EGN = EGN
        self.accounts = accounts

    def acc_loop(self):
        result = ""
        for acc in self.accounts:
            result += f"{acc.print_account()}"
        return result

    def print_user(self):
        return f"User({self.names}, {self.EGN}, {self.acc_loop()})"