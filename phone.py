from item import Item

class Phone(Item):
    def __init__(self,name: str, price: float, quantity=1,broken_phones=0):
        # Calls function super to get all attributes / methods
        super().__init__(
            name,price,quantity
        )
        # Validantion of parameter
        assert broken_phones >= 0, f"Quantity must be greater or equal to 0, got {broken_phones}"
        
        # Putting parameters for every instance
        
        self.broken_phones = broken_phones