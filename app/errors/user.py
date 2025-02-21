class UserError(Exception):
    """Base class for user-related errors."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class UserNotFoundError(UserError):
    """Exception raised when an user is not found."""
    def __init__(self, email: str = None):
        message = f"user with email {email} not found." if email else "user not found."
        super().__init__(message)
        
class UserAlreadyExistsError(UserError):
    def __init__(self, email):
        self.message = f"User with email {email} already exists."
        super().__init__(self.message)

class UserCreateError(UserError):
    """Exception raised when user creation fails."""
    def __init__(self, reason: str = "Unknown error"):
        message = f"User creation failed: {reason}."
        super().__init__(message)

class UserUpdateError(UserError):
    """Exception raised when user update fails."""
    def __init__(self, email: str = None, reason: str = "Unknown error"):
        message = (
            f"Failed to update User with email {email}: {reason}."
            if email
            else f"Failed to update user: {reason}."
        )
        super().__init__(message)

class UserDeleteError(UserError):
    """Exception raised when user deletion fails."""
    def __init__(self, email: int = None, reason: str = "Unknown error"):
        message = (
            f"Failed to delete user with email {email}: {reason}."
            if email
            else f"Failed to delete user: {reason}."
        )
        super().__init__(message)
