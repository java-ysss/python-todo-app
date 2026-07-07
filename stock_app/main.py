
from stock_manager import Stock_Manager
from datetime import datetime
def input_int(message):
        
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("数字を入力してください")
            continue


def input_required(message): #空文字を許さない
    while True:
        text = input(message)

        if text.strip() != "":  ## textが ""（空文字）と等しくないなら (.storip()は前後のスペースを取り除く)
            return text.strip()
        
        print("入力してください")

def input_quantity(message): #整数入力

    while True:
        try:
            quantity = int(input(message))

            if quantity < 0:
                print("0以上を入力してください")
                continue

            return quantity
        
        except ValueError:
            print("数字を入力してください")



def main():

    manager = Stock_Manager()
    manager.load_stocks()
    

    while True:

        print("=== 在庫管理 ===")

        menus = [
            "在庫追加",
            "在庫一覧",
            "在庫検索",
            "部分検索",
            "在庫削除",
            "在庫編集",
            "在庫数が多い順に表示",
            "商品名順に表示",
            "価格順に表示",
            "総在庫数",
            "最高額の在庫を表示",
            "総在庫金額",
            "100円以上の商品を表示",
            "個数と価格検索",
            "100円以下の商品を表示",
            "最低価格と最高価格検索",
            "csvから読み込み",
            "csv書き出し"
        ]

        for i,menu in enumerate(menus,start=1):
            print(f"{i} : {menu}")

        print("0 : 終了")
       
        choice = input_int("選択してください")

        if not 0<= choice <= len(menus):
            print("表示されている数字から選んでください")
            continue
        
        if choice == 1:
            
            name = input_required("名前を入力 > ")
            quantity = input_quantity("個数を入力 > ")
            price = input_quantity("金額を入力 > ")

            stock = manager.add_stock(name,quantity,price)

            if stock:
                print("追加できました")
                manager.save_stocks()
            else:
                print("追加できませんでした")

        elif choice == 2: #一覧

            manager.show_stock()

        elif choice == 3: #検索

            stock_id = input_int("IDを入力してください")

            stock = manager.search_stock(stock_id)

            if stock:
                print("見つかりました")
                print(stock)
            else:
                print("見つかりませんでした!")


        elif choice == 4: #部分検索

            keyword = input_required("部分検索 > ")

            stock = manager.partial_search_stock(keyword)

            if stock:
                print("ヒットしました")
                print(stock)
            else:
                print("該当する物は見つかりませんでした")
            

       
        elif choice == 5: #削除

            manager.show_stock()

            stock_id = input_int("削除するIDを入力してください")

            stock = manager.search_stock(stock_id)

            if not stock:
                print("見つかりませんでした")
                continue

            manager.delete_stock(stock_id)
            manager.save_stocks()
            print("削除しました")

        elif choice == 6: #編集

            manager.show_stock()

            stock_id = input_int("編集するIDを選んでください")

            stock = manager.search_stock(stock_id)

            if not stock:
                print("見つかりませんでした")
                continue

            name = input_required("新しい品名 > ")
            quantity = input_quantity("新しい個数 > ")
            price = input_quantity("新しい金額 > ")
            

            manager.edit_stock(stock_id,name,quantity,price)
            manager.save_stocks()
            print("変更しました")


        elif choice == 7: #在庫多い順

            stocks = manager.sorted_stocks()

            for stock in stocks:
                print(f"名前 : {stock.name} 在庫 : {stock.quantity}")


        elif choice == 8: #名前順

            stocks = manager.name_sorted_stocks()

            for stock in stocks:
                print(f"名前 : {stock.name} 在庫 : {stock.quantity}")
            


        elif choice == 9: #価格順
            
            stocks = manager.price_sorted_stocks()

            for stock in stocks:
                print(f"名前 : {stock.name} 価格 : {stock.price} 円 個数 {stock.quantity}")

        elif choice == 10: #総在庫数
            
            stock = manager.total_quantity()

            print(f"総在庫数 : {stock} 個")

        elif choice == 11: #一番高い在庫
            
            high_stock = manager.high_price()

            if high_stock:
                print(high_stock)
            else:
                print("見つかりませんでした")
            

        elif choice == 12: #総在庫金額

            stock = manager.total_price()

            print(f"総在庫金額 {stock} 円")
            
        elif choice == 13: #100円以上だけ表示

            result = manager.filter_by_price()

            if result:
                print(f"在庫名 : {result.name} : 価格 : {result.price}円")
            else:
                print("100円以上の在庫は見つかりませんでした")
            

        elif choice == 14: #個数と価格検索

            min_price = input_quantity("最低価格 > ")
            min_quantity = input_quantity("最低在庫数 > ")

            stocks = manager.fileter_stock(min_price,min_quantity)

            if stocks:
                for stock in stocks:
                    print(f"商品名 : {stock.name} 在庫数 : {stock.quantity} 価格 : {stock.price}")
            else:
                print("該当する商品は０件" \
                "条件を変更してみてください")


        elif choice == 15: #100円以下の商品を表示

            stocks = manager.filter_min_price()

            if stocks:
                for stock in stocks:
                    print(f"名前 : {stock.name} 価格 : {stock.price} 在庫 : {stock.quantity}")
            else:
                print("100円以下の商品はありませんでした")
            


        elif choice == 16: #最低価格～最高価格で検索

            min_price = input_quantity("最低価格を入力 > ")
            max_price = input_quantity("最高価格を入力 > ")

            if max_price < min_price:
                print("最低価格は最高価格以下で入力してください")
                continue

            stocks = manager.max_min_price(min_price,max_price)

            if stocks:
                for stock in stocks:
                    print(f"名前 : {stock.name} 価格 : {stock.price} 在庫 : {stock.quantity}")
            
            else:
                print("検索した商品は見つかりませんでした")


        elif choice == 17: #csv読み込み

            success_count , errors = manager.import_stock_csv("stocks.csv")

            print(f"{success_count}件読み込みました")

            if errors:
                print("===== エラー =====")

                with open("error.log","a",encoding="utf-8")as f: # errorsリストの中身を全部保存

                    for error in errors: #出力と保存　今回は同時にやる
                        now = datetime.now() #nowはループの中でOK
                        #これが“実務ログの基本形” ↓↓
                        log = f" [{now.strftime('%Y-%m-%d %H:%M:%S')}] {error}"

                        print(log) #出力
                        f.write(log + "\n") #ファイルに書く命令    "\n" : 改行を入れてる

        elif choice == 18: #csv書き出し(アプリのデータを外部ファイルへ出力)
            manager.export_stock_csv("stocks.csv")
            print("stocks.csv に書き出しました")




        elif choice == 0: #終了
            print("終了します")
            break
            

main()



