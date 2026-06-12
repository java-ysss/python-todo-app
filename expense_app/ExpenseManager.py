
import json
from Expense import Expense

class ExpenseManager:

    def __init__(self):
        self.expenses = []


    def add_expense(self,expense):#加えるメソッド
        self.expenses.append(expense)


    def show_expenses(self): #一覧表示メソッド

        if len(self.expenses) == 0:
            print("登録がありません")
        else:
            for index, expense in enumerate(self.expenses,start=1):
                print(f"{index} : {expense}") 

    def total_amount(self): #合計計算メソッド

        total = 0

        for expense in self.expenses:
            total += expense.amount

        return total
    
    def delete_expense(self,number): #削除メソッド

        if 0 <= number < len(self.expenses):
            remove = self.expenses.pop(number)
            print(f"{remove} を削除しました")
        else:
            print("指定した番号はありませんでした")

    def search_genre(self,genre): #ジャンル検索

        for expense in self.expenses:

            if genre == expense.genre:
                print(expense)

    def edit_expense(self,index,amount,day,item,genre): #編集メソッド
        
        if 0 <= index < len(self.expenses):

            expense = self.expenses[index - 1]

            expense.amount = amount
            expense.day = day
            expense.item = item
            expense.genre = genre

    def save_expenses(self):
        data = [expense.to_dict() for expense in self.expenses] #「家計簿の中身（Expenseたち）を全部、辞書に変換したリストを作る

        with open("expense.json" , "w", encoding = "utf-8")as file:
            json.dump(data,file,ensure_ascii=False,indent=4)
        #json.dump(data,file) は　PythonのデータをJSONファイルに書き込む
        #ensure_ascii=False 日本語を文字化けさせない indent=4 は見やすく整形


    def load_expenses(self):
        try:
            with open("expense.json","r",encoding="utf-8")as file:
                data = json.load(file)

                for item in data:
                    #print(f"読み込み中 : {item}")
                    expense = Expense( #取り出すときはいつでも[]を使う
                        item["amount"],
                        item["day"],
                        item["item"],
                        item["genre"]
                    ) #辞書から値を取り出して、Expenseオブジェクトを作り、それを expense に代入している

                    self.expenses.append(expense)
        except FileNotFoundError:
            pass #ファイルがなければ何もしない

#======================================================

#expense = Expense(...) 「Expenseクラスから家計簿データ1件を作る」

# json.dump(data, file)                              # 最低限これだけでも動く
# json.dump(data, file, ensure_ascii=False)          # 日本語を文字化けさせない
# json.dump(data, file, ensure_ascii=False, indent=4) # さらに見やすく整形S

