class Bank:
    def __init__(self, users):
        self.users = users

    def add_user(self, user):
        return self.users.append(user)
