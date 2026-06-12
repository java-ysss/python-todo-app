from ItemManger import ItemManager
from Item import Item


def main():

    manager = ItemManager()

    manager.load_items()
    
    while True:
        print("=== 在庫管理 ===")

        print("1 : 追加")
        print("2 : 一覧")
        print("3 : 削除")
        print("4 : 編集")
        print("5 : 検索")
        print("6 : 在庫が少ない商品表示")
        print("7 : 商品名順に並び替え")
        print("8 : 在庫順に並び替え")
        print("0 : 終了")

        
        try:
            choice = int(input("選んでください"))
        except ValueError:
            print("数字を選んでください")
            continue

        if 0 <= choice <= 8:

            if choice == 1:
                name = input("商品名 : ")
                try:
                    quantity = int(input("個数 : "))
                except ValueError:
                    print("数字を入力してください")
                    continue

                item = Item(name,quantity)

                manager.add_item(item)
                manager.save_items()

            elif choice == 2:

                manager.show_item()

            elif choice == 3:
                manager.show_item()

                while True:
                    try:
                        number = int(input("削除する番号を入力してください"))
                    except ValueError:
                        print("数字を入力してください")
                        continue


                    if manager.delete_item(number):
                        manager.save_items()
                        break
                    else:
                        print("その番号はありません")
                        continue
                    
                

            elif choice == 4:

                manager.show_item()

                while True:
                        
                    try:
                        number = int(input("編集する番号を選んでください"))
                    except ValueError:
                        print("数字を入力してください")
                        continue

                    if not (1 <= number <= len(manager.items)):
                        print("リストにあるものから選んでください")
                        continue
                        
                    name = input("変更名 > ")

                    try:
                        quantity = int(input("変更後の数 > "))
                    except ValueError:
                        print("数字を入力してください")
                        continue
                    
                    if manager.edit_item(number,name,quantity):
                        manager.save_items()
                        break
                    else:
                        print("リストにあるものから選んでください")
                        continue

            elif choice == 5:

                name = input("検索する商品名 > ")
                print("============================")

                manager.search_item(name)

            elif choice == 6:
                    
                try:
                    limit = int(input("在庫数の上限を入力してください > "))
                except ValueError:
                    print("数字を入力してください")
                    continue

                manager.show_low_item(limit)
            

            elif choice == 7:
                manager.sort_item()

                manager.show_item()
            elif choice == 8:
                manager.sort_quantity()

                manager.show_item()

            elif choice == 0:
                print("終了します")
                manager.save_items()
                break
        else:
            print("範囲の数字を入力してください")
            continue


main()