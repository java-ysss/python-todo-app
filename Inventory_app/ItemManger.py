import json
import os #Pythonに最初から入っている「OSを操作する機能の集まり」を使えるようにする宣言
from Item import Item

FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "items.json"
)

class ItemManager: #「複数の Item オブジェクトを管理するクラス」

    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def show_item(self):

        if len(self.items) == 0:
            print("在庫がありません")
            return
        
        for i, item in enumerate(self.items,start=1):
            print(f" {i} : {item}")


    def delete_item(self,number):   

        if 1 <= number <= len(self.items):
            self.items.pop(number - 1)
            return True
        else:
            return False


    def edit_item(self,number,name,quantity):

        if 1 <= number <= len(self.items):
            item = self.items[number - 1]

            item.name = name

            item.quantity = quantity
            return True
        else:
            return False
        
    def search_item(self,name):

        found = False
        for item in self.items:
            if item.name == name:
                print(f"{item.name} : {item.quantity}")
                found = True
            
        if not found:
            print("該当するものがありません")


    def show_low_item(self,limit):
        found = False

        for item in self.items:
            if item.quantity <= limit:
                print(f"{item.name} : {item.quantity}")
                found = True
            
        if not found:
            print("ありませんでした")

    def sort_item(self): #名前順

        self.items.sort(
            key=lambda item: item.name
        )
    
    def sort_quantity(self): #個数順
        self.items.sort(
            key=lambda item: item.quantity
        )
    

            
    

    def save_items(self):

        data = [item.to_dict() for item in self.items] #self.items の中にある Itemオブジェクトを1個ずつ取り出して、to_dict()で辞書に変換し、その結果をリストにする

        with open(FILE_PATH,"w",encoding="utf-8")as file: #保存用にファイルを開く
            json.dump(data,file) #data を JSON としてファイルに保存する



    def load_items(self):

        if os.path.exists(FILE_PATH) == False: #ファイルが無かったら何もしないで終了
            return

        with open(FILE_PATH,"r",encoding="utf-8")as file: #読み込みモードでファイルを開く

            data = json.load(file) #JSONファイルを読み込んで dict のリストにする

            for item in data: #dictを1個ずつ取り出す

                new_item = Item( #dictからItemオブジェクトを作る

                    item["name"],
                    item["quantity"]
                )
            
                self.items.append(new_item) #Itemオブジェクトをリストに追加する


#=================================================
#[item.to_dict() for item in self.items]
# Itemオブジェクト
# ↓
# 辞書
# ↓
# 辞書のリスト
# ↓
# JSONファイル

# save_items()
# Item
# ↓
# dict
# ↓
# JSON保存

#流れを理解

# load_items()
# JSON
# ↓
# dict
# ↓
# Item
