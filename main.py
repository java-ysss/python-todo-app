tasks = []

def save_tasks(tasks): #タスクのリストを受け取る関数を定義
      with open("tasks.txt","w",encoding = "utf-8")as file: #下に意味を書いてる

        for task in tasks: #タスクリストを1つずつ取り出す
              file.write(task + "\n")

def load_tasks():

def input_task():
        task = input("タスク名 >  ")
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


def add_task(tasks,task):
        tasks.append(task)
        #リストの末尾に要素を追加するメソッド


def delete_task(tasks):
        for i,task in enumerate(tasks,start=1):# 入力された番号が 1以上かつタスクの総数以下 かチェック
                print(i,task) #enumerate()は、リストなどの要素をインデックス番号付きで取り出す関数

        try:
                delete_num = int(input("削除番号 > "))

                if 1 <= delete_num <= len(tasks): #delete_numが1以上、かつtasksの長さ以下かどうか」
                    tasks.pop(delete_num - 1)  #pop()は、リストから要素を取り出して削除するメソッド
                else:
                    print("その番号はありません")

        except ValueError:
                    print("数字を入力してください")

def edit_task(tasks):
      
      if not tasks:
            print("タスクがありません")
      else:
            for i,task in enumerate(tasks,start=1):
                    print(i,task)


      edit_num = int(input("編集番号 > "))

      if 1 <= edit_num <= len(tasks):

        new_task = input("新しいタスク名 > ")

        tasks[edit_num - 1] = new_task #「リストの特定位置を操作する」

def main():
        while True:
                
            print("1 : 追加")
            print("2 : 表示")
            print("3 : 削除")
            print("4 : 編集")
            print("5 : 終了")

            choice = input("選んでください >  ")

            if choice == "1":
                task = input_task()
                add_task(tasks,task)

            elif choice == "2":
                show_tasks(tasks)

            elif choice == "3":
                delete_task(tasks)

            elif choice == "4":

                edit_task(tasks)

            elif choice == "5":
                save_tasks(tasks)

                break

main()


#withは「後片付けを自動化する仕組み」って考えるとかなり理解しやすい。
#open("tasks.txt")  tasks.txt というファイルを開く（なければ新規作成）
# "w"  書き込みモード（上書き）
# encoding="utf-8" 日本語が文字化けしないようにする
# as file  開いたファイルを file という名前で使う
# with  処理が終わったら自動でファイルを閉じてくれる
#file.write()  ファイルに文字を書き込む
# + "\n"  改行を追加（これがないと全部1行になる）
