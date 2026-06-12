
from Expense import Expense
from ExpenseManager import ExpenseManager

def main():

    
    manager = ExpenseManager() #ExpenseManagerクラスのインスタンス（実体）を作っている
    manager.load_expenses()

    while True:
        print("1 : 支出追加")
        print("2 : 一覧表示")
        print("3 : 合計表示")
        print("4 : 削除")
        print("5 : ジャンル検索")
        print("6 : 編集")
        print("0 : 終了")
        try:
            choice = int(input("選んでください"))
        except ValueError:
                print("数字を入力してください")
                continue

        if choice == 1:
            while True:
                try:
                    amount = int(input("金額 : "))
                    break
                except ValueError:
                        print("数字を入力してください")
                        continue
                
            day = input("日付 : ")
            item = input("品物 : ")
            genre = input("ジャンル : ")

            expense = Expense(amount,day,item,genre)

            manager.add_expense(expense)

            manager.save_expenses()

        elif choice == 2:
                print("--------------------------")

                manager.show_expenses()

                print("--------------------------")
        elif choice ==  3:
                print(f"合計 : {manager.total_amount()} 円")

        elif choice ==  4:
                manager.show_expenses()

                number = int(input("削除番号を選んでください"))

                manager.delete_expense(number - 1)

                manager.save_expenses()

        elif choice == 5:
                genre = input("ジャンル : ")

                manager.search_genre(genre)

        elif choice == 6:
                
            manager.show_expenses()
            
            print("=======================")
            while True:
                try:
                    index = int(input("編集する家計簿を選んでください > "))
                    break
                except ValueError:
                        print("数字を入力してください")
                        continue

            while True:
                try:
                    amount = int(input("金額 : "))
                    break
                except ValueError:
                    print("数字を入力してください")
                    continue
            day = input("日付 : ")
            item = input("品物 : ")
            genre = input("ジャンル : ")

            manager.edit_expense(index,amount,day,item,genre)

            manager.save_expenses()

        elif choice == 0:
                    break
        else:
            print("もう一度入力し直してください")
            continue


main()
