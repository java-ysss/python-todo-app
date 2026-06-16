from sale import Sale
import json
import os

class SaleManager:

    def __init__(self):
        self.sales = []

    def add_sale(self,sale): #追加メソッド
        self.sales.append(sale)

    def show_sale(self): #表示メソッド

        if len(self.sales) == 0:
            print("売上はありません")
            return

        for i, sele in enumerate(self.sales,start=1):
            print(f"{i} : {sele}")

    def delete_sale(self,number): #削除

        if 1 <= number <= len(self.sales):
            self.sales.pop(number - 1)
            return True
        else:
            return False
    
    def total_sales(self): #総売り上げ

        total = 0

        for sale in self.sales:
            total += sale.quantity * sale.price
    
        return total
    
    def search_sale(self,name): #検索

        found = False

        for sale in self.sales:
            if sale.name == name:
                print(f"{sale.date} : {sale.name} : {sale.quantity}個 {sale.price}円")
                found = True

        if not found:
            print("該当する者は見つかりませんでした")
        
        return found
    
    def edit_sale(self,number,date,name,quantity,price): #編集
            
        while True:

            if 1 <= number <= len(self.sales):
            
                sale = self.sales[number - 1]

                sale.date = date
                sale.name = name
                sale.quantity = quantity
                sale.price = price

                return True
            else:
                return False


    
    def save_sale(self): #保存

        data = [sale.to_dict() for sale in self.sales] # dict型に変えている

        with open("sales.json","w",encoding="utf-8")as file:
            json.dump(data,file,ensure_ascii=False,indent=4) #➀

    def load_sale(self): #読み込み

        if not os.path.exists("sales.json"): #これはセット(エラーを防ぐ)
            return
        
        self.sales = [] #一度空にして読み込むと重複しない

        with open("sales.json","r",encoding="utf-8")as file:
        
            data = json.load(file) # ➁ JSONファイルを読み込んで dict のリストに変換する

            for sale in data: ## dict から値を取り出して Sale オブジェクトを作る
                sale = Sale(
                    sale["date"], # item["date"] は dict の "date" キーの値を取り出している
                    sale["name"], # "りんご"
                    sale["quantity"], #１０個
                    sale["price"] # 100円
                )

                self.sales.append(sale) # 作った Sale オブジェクトをリストに追加する
            


#===============================================================-

#　➀　json.dump(data, file) PythonのデータをJSON形式でファイルに書き込む」 関数
# data（Pythonのデータ）をfile（JSONファイル）に吐き出す

# json.dump(data, file, ensure_ascii=False, indent=4)
# 〇　data              # 保存したいデータ（dictのリスト）
# 〇　file              # 書き込み先のファイル
# 〇　ensure_ascii=False # 日本語をそのまま保存する（Falseにしないと文字化けする）
# 〇　indent=4          # 見やすく整形する（スペース4つ分の字下げ）

# ➁ # data の中身はこういう状態 (dict型)
# [
#     {"date": "2024-01-01", "name": "りんご", "quantity": 10, "price": 100},
#     {"date": "2024-01-02", "name": "みかん", "quantity": 5,  "price": 200}
# ]