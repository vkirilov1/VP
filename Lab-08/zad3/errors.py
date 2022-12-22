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


class InvalidCharacterClass(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class CharacterExists(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class CharacterNotFound(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


