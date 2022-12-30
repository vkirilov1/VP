<<<<<<< HEAD
class InvalidCommand(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class InvalidDataFormat(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class InvalidAccCurrency(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class InvalidAccountType(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class UserNotFound(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class AccNotFound(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class NotEnoughMoney(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
=======
class InvalidCommand(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class InvalidDataFormat(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class InvalidAccCurrency(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class InvalidAccountType(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class UserNotFound(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class AccNotFound(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class NotEnoughMoney(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
>>>>>>> e75c3a72cc9faaba0c276e43501f5c8663310736
        return f"{self.message}"