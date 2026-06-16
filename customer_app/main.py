
from customer_manager import Customer_Manager
from customer import Customer


def main():


    manager = Customer_Manager()

    while True:

        print("=== 顧客管理 ===")

        print("1 : 顧客登録")
        print("2 : 顧客一覧")
        print("3 : 顧客検索")
        print("4 : 顧客削除")
        print("5 : 顧客編集")
        print("0 : 終了")

        

        try:
            choice = int(input("数字を入力してください"))
        except ValueError:
            print("数字を入力してください")
            continue

        if not 0 <= choice < 6:
            print("範囲内の数字を入力してください")
            continue


        if choice == 1:

            name = input("名前を入力 > ")
            try:
                phone = int(input("電話番号を入力 > "))
            except ValueError:
                print("数字を入力してください")
                continue

            email =  input("e-mailを入力 >")
        
            manager.add_customer(name,phone,email)

        elif choice == 2:

            manager.show_customer()

        elif choice == 3:

            name = input("検索する名前を入力 > ")

            results = manager.search_customer(name)

            if not results:
                print("見つかりませんでした")
            else:
                for customer in results:
                    print(customer)

        elif choice == 4:
            
            manager.show_customer()

            try:
                id = int(input("削除する顧客番号を入力 > "))
            except ValueError:
                print("数字を入力してください")
                continue

            if manager.delete_customer(id):
                print("削除しました")
            else:
                print("削除するデータがありません")

        elif choice == 5:

            manager.show_customer()

            try:
                id = int(input("編集する顧客番号を入力 > "))
            except ValueError:
                print("数字を入力してください")
                continue
            
            name = input("新しい名前 > ")

            try:
                phone = int(input("新しい番号 > "))
            except ValueError:
                print("数字を入力してください")
                continue

            email = input("新しいe-mailを入力 > ")

            if manager.edit_customer(id,name,phone,email):
                print("変更しました")
            else:
                print("その顧客データはありません")
                continue



        elif choice == 0:

            print("終了します")
            break




main()

