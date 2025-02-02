from item import Item

class Phone(Item):
    all = []
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )
        #Asserting the Values
        assert broken_phones >=0, f"Broken_phones:{broken_phones} is less than zero!"

        #Initialising Values
        self.broken_phones = broken_phones