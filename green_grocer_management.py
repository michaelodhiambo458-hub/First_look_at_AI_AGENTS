from abc import ABC, abstractmethod
class Produce(ABC):
    def __init__(self,name,quantity,price):
        self.name=name
        self.price=price
        self.quantity=quantity
    def get_validity(self):
         if self.name == "":
             raise ValueError("Name cannot be an empty string")
         if self.quantity <0:
             raise ValueError("Quantity can't be negative")
         if self.price <0:
             raise ValueError("Price can't be negative")
    @abstractmethod
    def get_unit(self):
        pass
class Vegetable(Produce):
    def __init__(self,name,quantity,price):
        super().__init__(name,quantity,price)   
    def get_unit(self):
        return f"Vegetable:{self.name}, Quantity:{self.quantity}Kg/Kg's"
class Shop(Produce):
    def __init__(self,inventory,name,quantity,price):
        super().__init__(name,quantity,price)
        self.inventory=[]
    def veg_items(self):
        produce=Vegetable
        self.inventory.append(produce)
    def __str__(self):
        for items in self.inventory:
            return f"{self.name} {self.quantity} {self.price}//n"