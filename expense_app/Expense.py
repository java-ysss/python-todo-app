

class Expense:

    def __init__(self,amount,day,item,genre):
        self.amount = amount
        self.day = day
        self.item = item
        self.genre = genre
    
    def __str__(self): #「このオブジェクトをどう表示する？」を決めるメソッド
        return f"{self.amount}円 {self.day} {self.item} {self.genre}"
    
    def to_dict(self): #jsonは辞書型にする必要がある オブジェクト → 辞書 → JSON
        return {
            "amount" : self.amount,
            "day" : self.day,
            "item" : self.item,
            "genre" : self.genre
        }