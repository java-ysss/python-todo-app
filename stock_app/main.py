
from stock_manager import Stock_Manager

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
            "価格順に表示"
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

            manager.add_stock(name,quantity,price)
            manager.save_stocks()

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

            
        elif choice == 0: #終了
            print("終了します")
            break

main()


