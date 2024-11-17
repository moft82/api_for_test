# errors/item.py

class ItemError(Exception):
    """Base class for item-related errors."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class ItemNotFoundError(ItemError):
    """Exception raised when an item is not found."""
    def __init__(self, item_id: int = None):
        message = f"Item with ID {item_id} not found." if item_id else "Item not found."
        super().__init__(message)

class ItemCreateError(ItemError):
    """Exception raised when item creation fails."""
    def __init__(self, reason: str = "Unknown error"):
        message = f"Item creation failed: {reason}."
        super().__init__(message)

class UpdateError(ItemError):
    """Exception raised when item update fails."""
    def __init__(self, item_id: int = None, reason: str = "Unknown error"):
        message = (
            f"Failed to update item with ID {item_id}: {reason}."
            if item_id
            else f"Failed to update item: {reason}."
        )
        super().__init__(message)

class DeleteError(ItemError):
    """Exception raised when item deletion fails."""
    def __init__(self, item_id: int = None, reason: str = "Unknown error"):
        message = (
            f"Failed to delete item with ID {item_id}: {reason}."
            if item_id
            else f"Failed to delete item: {reason}."
        )
        super().__init__(message)
