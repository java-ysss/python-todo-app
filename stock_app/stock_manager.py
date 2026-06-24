from stock import Stock
import json

class Stock_Manager:

    def __init__(self):
        self.stocks = []
        self.next_id = 1

    def add_stock(self,name,quantity,price): #追加

        stock = Stock(self.next_id,name,quantity,price)
        
        self.stocks.append(stock)
        self.next_id += 1
        

    def show_stock(self): #一覧

        if not self.stocks:
            print("在庫はありません")
            return 

        for stock in self.stocks:
            print(stock)

    def search_stock(self,stock_id):#検索 
        #「id が一致する Stock オブジェクトを探して、そのオブジェクトを stock 変数に入れる」

        for stock in self.stocks:
            if stock.id == stock_id:
                return stock
            
        return None


    def delete_stock(self,stock_id):  #削除

        stock = self.search_stock(stock_id)

        if stock:
            self.stocks.remove(stock)
            return True
        
        return False


    def edit_stock(self,stock_id,name,quantity,price): #編集

        stock = self.search_stock(stock_id)

        if not stock:
            return False
        
        stock.name = name
        stock.quantity = quantity
        stock.price = price

        return True
    
    def sorted_stocks(self): #多い順
        
        return sorted(
            self.stocks , key=lambda stock : stock.quantity ,
            reverse=True
        )
        #改良版

    def name_sorted_stocks(self): #名前順

        return sorted(
            self.stocks,key=lambda stock : stock.name ,
            #reverse=True 名前だと降順(Z ~ A)になるから消す
        )

    def price_sorted_stocks(self): #価格順

        return sorted(
            self.stocks, key=lambda stock : stock.price
        ) #今は安い順


    def partial_search_stock(self,keyword): #部分一致検索
       
        result = []
    
        for stock in self.stocks:

            if keyword in stock.name:
                result.append(stock)

        return result

    
    
        

    def save_stocks(self): #保存

        data = [stock.to_dict() for stock in self.stocks]

        with open("stocks.json","w",encoding="utf-8")as file:
            json.dump(data,file,ensure_ascii=False,indent=4)


    def load_stocks(self): #読み込み

        try: # 初回起動のエラーを防ぐために　try　を使う
            with open("stocks.json","r",encoding="utf-8")as file:
                data = json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            data = []
    #jsonが空の時に　エラーで落ちるのを防ぐ ↑　↓

        self.stocks = []

        for item in data:

            stock = Stock(
                item["id"],
                item["name"],
                item["quantity"],
                item["price"]
            )

            self.stocks.append(stock)

        if self.stocks: #「今あるIDの最大値に+1して、次のIDにする」という意味
            self.next_id = max(stock.id for stock in self.stocks) + 1 # (全stockのidの中で一番大きい数を取得する) + 1



#==============

# indent=4
# → インデント（字下げ）を4文字にする
# ensure_ascii=False
# → 日本語をそのまま保存する
    


# sorted(stocks, ...)
# 並び替えたいリストをそのまま渡しています。

# sorted() は元のリストを変えず、新しい並び替え済みリストを返します。


# sorted(stocks, key=lambda stock: stock.quantity, reverse=True)
# これは「stocksリストを、各要素のquantityを基準に、大きい順に並び替えて返す」というコード。


# key=lambda stock: stock.quantity
# key は「何を基準に並べるか」を指定するものです。
# lambda stock: stock.quantity は、こう読みます： # 「stockを受け取って、stock.quantityを返す関数」

# sorted() は各要素に対してこの関数を呼び出して、その戻り値（quantity）で比較します。


# reverse=True   # 大きい順（降順）
# reverse=False  # 小さい順（昇順）← デフォルト
# True にすると quantity が多い順に並びます。

# sorted(リスト, key=lambda 仮の名前: 仮の名前.属性, reverse=True)


