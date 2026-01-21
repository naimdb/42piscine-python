from S1E9 import Character

class Baratheon(Character):
    """
    Representing the Baratheon family.

    Attributes:
        first_name (str): The name of the Baratheon character.
        is_alive (bool): Status indicating if the character is alive. Default is True.
        family_name (str): The family name "Baratheon".
        eyes (str): The eye color "brown".
        hairs (str): The hair color "dark".
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character with a name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

class Lannister(Character):
    """
    Representing the Lannister family.

    Attributes:
        first_name (str): The name of the Lannister character.
        is_alive (bool): Status indicating if the character is alive. Default is True.
        family_name (str): The family name "Lannister".
        eyes (str): The eye color "blue".
        hairs (str): The hair color "light".
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character with a name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    
    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        return cls(first_name, is_alive)
         