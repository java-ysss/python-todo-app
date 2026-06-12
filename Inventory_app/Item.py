class Item:

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} : {self.quantity}個"
    
    def to_dict(self): #「クラスのデータを辞書に変換するメソッド」(dict型)
        return {
            "name" : self.name, #"name": self.name は**代入ではなく「セット」**
            "quantity" : self.quantity
        }
    

