<<<<<<< HEAD
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
=======
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
>>>>>>> e75c3a72cc9faaba0c276e43501f5c8663310736
        return f"User({self.names}, {self.EGN}, {self.acc_loop()})"