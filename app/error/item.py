# errors/item.py

class ItemNotFoundError(Exception):
    def __init__(self, item_id=None, user_id=None):
        self.message = f"Item with ID {item_id} not found for user {user_id}."
        super().__init__(self.message)

class FileNotFoundError(Exception):
    def __init__(self, file_path):
        self.message = f"File not found at path: {file_path}."
        super().__init__(self.message)

class InvalidFilePathError(Exception):
    def __init__(self, file_path):
        self.message = f"Invalid file path: {file_path}."
        super().__init__(self.message)

class UpdateError(Exception):
    def __init__(self, item_id=None):
        self.message = f"Failed to update item with ID {item_id}."
        super().__init__(self.message)

class DeleteError(Exception):
    def __init__(self, item_id=None):
        self.message = f"Failed to delete item with ID {item_id}."
        super().__init__(self.message)
