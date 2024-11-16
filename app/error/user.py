class UserAlreadyExistsError(Exception):
    def __init__(self, email):
        self.message = f"User with email {email} already exists."
        super().__init__(self.message)

class UserNotFoundError(Exception):
    def __init__(self, user_id):
        self.message = f"User with ID {user_id} not found."
        super().__init__(self.message)

class UserDeletionError(Exception):
    def __init__(self, user_id):
        self.message = f"Failed to delete user with ID {user_id}."
        super().__init__(self.message)