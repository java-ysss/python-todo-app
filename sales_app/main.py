from sale_manager import SaleManager
from sale import Sale

def main():

    manager = SaleManager() 
    manager.load_sale()

    while True:
        print("=== 売上管理 ===")

        print("1 : 追加")
        print("2 : 一覧")
        print("3 : 削除")
        print("4 : 総売り上げ表示")
        print("5 : 検索")
        print("6 : 編集")
        print("0 : 終了")

        try:
            choice = int(input("選んでください > "))
        except ValueError:
            print("数字を入力してください")
            continue


        if choice == 1:

            date = input("日付(例:2025-03-29) > ")
            name = input("商品名 > ")

            try:
                quantity = int(input("個数 > "))
            except ValueError:
                print("数字を入力して下さい")
                continue
                
            try:
                price = int(input("価格 > "))
            except ValueError:
                print("数字を入力してください")
                continue

            sale = Sale(date,name,quantity,price)

            manager.add_sale(sale)
            manager.save_sale()

        elif choice == 2:

            manager.show_sale()

        elif choice == 3:

            if len(manager.sales) == 0:
                print("削除できるデータがありません")
                continue

            while True:
                manager.show_sale()
                try:
                    number = int(input("削除する項目を選んでください"))
                except ValueError:
                    print("数字で入力してください")
                    continue
                    
                if manager.delete_sale(number):

                    manager.save_sale()
                    break
                else:
                    print("表示されている数字から選んで下さい")
                    continue


        elif choice == 4: #総売り上げ
            total = manager.total_sales()

            print(f"総売り上げ : {total}円")


        elif choice == 5: #検索
            
            name = input("調べたい商品名を入力してください")

            manager.search_sale(name)

        elif choice == 6: #編集

            if len(manager.sales) == 0:
                print("編集できるデータがありません")
                break

            while True:
                manager.show_sale()

                try:
                    number = int(input("== 編集したい番号を選んでください =="))
                except ValueError:
                    print("数字で入力してください")
                    continue

                date = input("新しい日付 > ")
                name = input("新しい商品名 > ")
                try:
                    quantity = int(input("新しい個数 > "))
                except ValueError:
                    print("数字を入力してください")
                    continue
                
                try:
                    price = int(input("新しい価格 > "))
                except ValueError:
                    print("数字を入力してください")
                    continue

                if manager.edit_sale(number,date,name,quantity,price):
                    manager.save_sale()
                    break
                else:
                    print("表示されたものの数字を入力してください")
                    continue
                


            

        elif choice == 0:
            print("終了します")
            break









if __name__== "__main__": #「このファイルが直接実行されたときだけ main() を呼ぶ」という意味
    main()