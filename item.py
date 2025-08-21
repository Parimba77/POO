import csv

class Item():
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name: str, price: float, quantity=1):
        # Validantion of parameter
        assert price >= 0, f"Price must be greater or equal to 0, got {price}"
        assert quantity >= 0, f"Quantity must be greater or equal to 0, got {quantity}"
        
        #Putting parameters for every instance
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    # Property attribue, read only
    @property
    def name(self):
        return self.__name
    
    # Putting the read only parameter to a value so you can modify it.
    @name.setter
    def name(self,value):
        if len(value) > 15:
            raise Exception("Name too longe!")
        else:
            self.__name = value
    
    #Executives
    def calculate_price(self):
        return self.price * self.quantity
        
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    #Reading the csv file
    @classmethod    
    def instantiate_from_csv(cls):
        with open ("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name= item.get("name"),
                price= float(item.get("price")),
                quantity= int(item.get("quantity"))
            )
            
    #Checking if number is integer
    @staticmethod
    def is_integer(num):
        
        if isinstance(num, float):
            return num.is_integer()
        
        elif isinstance(num, int):
            return True
        
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

