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
        self.__price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    @property
    def price(self):
        return self.__price    
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    # Property attribue, read only
    @property
    def name(self):
        return self.__name
    
    def aply_increment(self,increment):
        self.__price = self.__price + self.__price * increment
    
    # Putting the read only parameter to a value so you can modify it.
    @name.setter
    def name(self,value):
        if len(value) > 15:
            raise Exception("Name too longe!")
        else:
            self.__name = value
    
    #Executives
    def calculate_price(self):
        return self.__price * self.quantity
        
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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    def __connect(self, smtp_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello, 
        We have {self.name} {self.quantity} times.
        Regards, 
        The team.
        """
    
    def __send(self):
        pass

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()