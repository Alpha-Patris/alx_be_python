import csv

class Item:
    all = []
    def __init__(self, name:str, price:float, quantity=0):
        #Asserting the Values
        assert price >= 0, f"Price:{price} is less than zero!"
        assert quantity >=0, f"Quantity:{quantity} is less than zero!"

        #Initialising Values
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.price_total = price * quantity

        #Actions to execute
        Item.all.append(self)

     #Instanciating values from csv file
    @classmethod
    def instantiate_from_csv(cls):
        with open('store.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('Name'),
                price = float(item.get('Price')),
                quantity = float(item.get('Quantity'))
            )
    
    @property
    #Property Decorator = Read-only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception ("Name is too long!")
        else:
            self.__name = value 

    @staticmethod
    def isinteger(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else: return False
        
    def __str__(self):
        return f"Item: {self.name} Price: sh{self.price} Stock Value: sh{self.price_total}"
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"