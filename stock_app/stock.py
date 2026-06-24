
class Stock:

    def __init__(self,id,name,quantity,price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price


    def __str__(self): #str は 「printされたときの見た目担当」
        return f"ID : {self.id} 商品名 : {self.name} 個数 : {self.quantity} 個 価格 : {self.price} 円 : 合計 {self.get_total_price()}"
    

    def get_total_price(self):

        total = self.quantity * self.price

        return total
    
    def to_dict(self): #オブジェクト → 辞書(dict)
        return {
            "id" : self.id,
            "name" : self.name,
            "quantity" : self.quantity,
            "price" : self.price

        }
    


    