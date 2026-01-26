from abc import ABC, abstractmethod


class Character(ABC):
    """
    A base class representing a character in a story.

    Attributes:
        first_name (str): The name of the character.
        is_alive (bool):
        Status indicating if the character is alive. Default is True.

    Methods:
        die(): Sets the character's is_alive status to False.
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Character with a name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set the character's status to not alive."""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the character."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Return an official string representation of the character."""
        return f"{type(self).__name__}('{self.first_name}',\
            is_alive={self.is_alive})"


class Stark(Character):
    """
    Representing the Stark family.

    Attributes:
        first_name (str): The name of the Stark character.
        is_alive (bool):
        Status indicating if the character is alive. Default is True.
    """

    def __init__(self, name: str, is_alive: bool = True):
        """Initialize a Stark character with a name and alive status."""
        super().__init__(name, is_alive)
