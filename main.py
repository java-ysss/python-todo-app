tasks = []

def input_task():
        task = input("タスク名 > ")
        return task
    #関数の結果を外で使いたい？
    #YES → return 必要
    #NO → return なくてもOK

def show_tasks(tasks):
        if not tasks:
                print("タスクがありません")
        else:
                for i,task in enumerate(tasks,start=1):
                    print(i,task)


def add_task(task):
        tasks.append(task)
        #リストの末尾に要素を追加するメソッド


def delete_task():
        for i,task in enumerate(tasks,start=1):
    # 入力された番号が 1以上かつタスクの総数以下 かチェック
                print(i,task)
    #enumerate()は、リストなどの要素をインデックス番号付きで取り出す関数
                try:

                    delete_num = int(input("削除番号 > "))

                    if 1 <= delete_num <= len(tasks):
                        tasks.pop(delete_num - 1)
    #pop()は、リストから要素を取り出して削除するメソッド

                    else:
                        print("その番号はありません")

                except ValueError:
                    print("数字を入力してください")

def main():
        while True:
                
            print("1:追加")
            print("2:表示")
            print("3:削除")
            print("4:終了")

            choice = input("選んでください >")

            if choice == "1":
                task = input_task()
                add_task(task)

            elif choice == "2":

                show_tasks(tasks)

                #start=1 は番号を1から始めてください


            elif choice == "3":
                delete_task()

            elif choice == "4":
                break

main()
