from stock import Stock
import json

class Stock_Manager:

    def __init__(self):
        self.stocks = []
        self.next_id = 1

    
    def import_stock_csv(self,file_path):#csv読み込み

        with open(file_path,"r", encoding="utf-8")as file:
            lines = file.readlines() #readlines() でファイルの中身を1行ずつリストにする

        count = 0

        errors = []

        for line_num , line in enumerate(lines[1: ],start=2):
            data = line.strip().split(",")
            # .strip() → 行末の改行 \n を消す
            # .split(",") → カンマで分割してリストに変換

            #stock_id = int(data[0])

            if len(data) != 3:
                errors.append(f"{line_num}行目で不足している項目があります")
                continue

            name = data[0]

            try:
                quantity = int(data[1])
                price = int(data[2])
                #数値として使いたい id, quantity, price は str → int() で変換する
            except ValueError:
                errors.append(f"{line_num}行目 : 個数または価格が不正です({line.strip()})")
                continue

            is_valid , message = self.validate_stock(name,quantity,price) #falseならTrueになる
            
            if not is_valid:
                print(message)
                errors.append(f"{line_num}行目 : {message}")
                continue #エラーがあっても止めない

            if self.add_stock(name,quantity,price):
            #self.stocks.append(stock)
                count += 1

        if self.stocks:
            self.next_id = max(stock.id for stock in self.stocks) + 1

        
        return count , errors
    

    def export_stock_csv(self,file_path): #内部から→外部(csv書き出し)
        #file_path は　仮引数名
        with open(file_path,"w",encoding="utf-8")as file:
            file.write("name,quantity,price\n") #これがヘッダー行


            for stock in self.stocks:
                line = f"{stock.name},{stock.quantity},{stock.price}" #1行分の文字列
                file.write(line + "\n") #改行付きで書き込む



    def add_stock(self,name,quantity,price): #追加

        is_valid,message = self.validate_stock(name,quantity,price) #チェックは必要

        if not is_valid: #判定結果がFalseなら
            print(message)
            return False

        stock = Stock(self.next_id,name,quantity,price)
        
        self.stocks.append(stock)
        self.next_id += 1

        return True
        

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

        if stock is None:
            return False
        
        self.stocks.remove(stock)
        return True


    def edit_stock(self,stock_id,name,quantity,price): #編集

        stock = self.search_stock(stock_id)

        if stock is None:
            return False
        
        is_valid,message = self.validate_stock(name,quantity,price) #()の中に２つの真偽値　分ける必要がある

        if not is_valid:
            print(message)
            return False
        
        stock.name = name
        stock.quantity = quantity
        stock.price = price

        return True


    def validate_stock(self,name,quantity,price): #「このデータ、使っても大丈夫?」をチェックする処理

        if not name:
            return False , "名前が空です"
        
        if quantity < 0:
            return False , "個数を0未満にできません"
        
        if price < 0:
            return False , "価格を0未満にできません"
        

        return True ,""
    

    
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
        # result = []
        # for stock in self.stocks:
        #     if keyword in stock.name:
        #         result.append(stock)
        # return result

        return [stock for stock in self.stocks if keyword in stock.name]
    
    
    def total_quantity(self): #総在庫数

        total = 0

        for stock in self.stocks:

            total += stock.quantity 

        return total
        # def total_quantity(self):　sumを使うと短くなる(合計を求める関数)
        #      return sum(stock.quantity for stock in self.stocks)

 
    def total_price(self): #総在庫金額

        total = 0

        for stock in self.stocks:

            total += stock.price

        return total

    
    def high_price(self): #最高額一つ

        return max(self.stocks,key=lambda stock : stock.price) 
                    #price が最大の Stockオブジェクトを返して

        
    def filter_by_price(self): #100円以上の商品だけ表示
        # result = []
        # for stock in self.stocks:
        #     if stock.price >= 100:
        #         result.append(stock) #ここはオブジェクトを返す
        # return result

        return [stock for stock in self.stocks if stock.price >= 100]
    
    
    def fileter_stock(self,min_price,min_quantity): #最低価格、在庫検索
    #     result = []
    #     for stock in self.stocks:
    #         if min_price <= stock.price and stock.quantity >= min_quantity:
    #             result.append(stock)
    #     return result

        return [stock for stock in self.stocks if min_price <= stock.price and stock.quantity >= min_quantity]
            # #「商品の価格が、ユーザーが入力した最低価格以上で、さらに商品の在庫数が、ユーザーが入力した最低在庫数以上なら」

    

    def filter_min_price(self): #100円以下の商品を表示
        # result = []
        # for stock in self.stocks:
        #     if stock.price <= 100:
        #         result.append(stock)
        # return result

        return [stock for stock in self.stocks if stock.price <= 100]
    
        

    
    def max_min_price(self,min_price,max_price):#価格上限下限検索
        # result = []
        # for stock in self.stocks:
        #     if min_price <= stock.price and stock.price <= max_price:
        #         result.append(stock)
        # return result

        return [stock for stock in self.stocks if min_price <= stock.price <= max_price]



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

# lambda 引数 : 返す値
#          ↑        ↑
#     受け取るもの  処理結果

