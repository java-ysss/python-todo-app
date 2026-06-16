
class Sale:

    def __init__(self,date,name,quantity,price):
        self.date = date
        self.name = name
        self.quantity = quantity
        self.price = price
        


    def __str__(self):
        total = self.quantity * self.price
        return f"{self.date} : {self.name} : {self.quantity}個 : {self.price}円 : {total}円"
    
    def to_dict(self):
        return{
            "date" : self.date,
            "name" : self.name,
            "quantity" : self.quantity,
            "price" : self.price
        }
