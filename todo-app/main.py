

from manager import Manager #manager はファイル名　Managerはクラス名



def input_task(message = "タスク名 : "):

        while True:
            
            task = input(message ).strip() #空白だけ入力も防げる。

            if task: #空文字 → False | 文字あり → True
                return task
            
            print("空入力できません")

    #関数の結果を外で使いたい？
    #YES → return 必要
    #NO → return なくてもOK

def input_number(message):#番号入力関数

      while True:

            try:
                  return int(input(message))

            except ValueError:
                  print("数字を入力してください")



#==============================================================



def main():
        
        manager_data = Manager()
        manager_data.load_tasks()

        while True:
                
            print("1 : 追加 ")
            print("2 : 表示 ")
            print("3 : 削除 ")
            print("4 : 編集 ")
            print("5 : 完了切り替え ")
            print("6 : 完了済み削除 ")
            print("7 : 終了 ")


            choice = input("選んでください >  ")

            if choice == "1":
                task = input_task()
                manager_data.add_task(task)

            elif choice == "2":
                manager_data.show_tasks()

            elif choice == "3":
                num = input_number("削除番号 > ")
                manager_data.delete_task(num)

            elif choice == "4":
                manager_data.show_tasks()
                num = input_number("編集番号 > ")
                new_name = input_task("新しいタスク名 > ")
                manager_data.edit_task(num,new_name)



            elif choice == "5":
                  
                  manager_data.show_tasks()
                  num = input_number("完了切り替え番号 > ")
                  manager_data.toggle_task(num)


            elif choice == "6":
                 
                manager_data.delete_done_tasks()
            

            elif choice == "7":

                break


if __name__ == "__main__": #このファイルが直接実行されたときだけ、以下のコードを動かす、という意味
      main()  # メインの処理を開始する

      #全体の意味はこのスクリプトが直接起動されたら、タスクを読み込んで、メイン処理を実行する」


#withは「後片付けを自動化する仕組み」って考えるとかなり理解しやすい。
# with open("tasks.txt","w",encoding = "utf-8")as file:
#open("tasks.txt")  tasks.txt というファイルを開く（なければ新規作成）
# "w"  書き込みモード（上書き）
# encoding="utf-8" 日本語が文字化けしないようにする
# as file  開いたファイルを file という名前で使う
# with  処理が終わったら自動でファイルを閉じてくれる
#file.write()  ファイルに文字を書き込む
# { + "\n" }  改行を追加（これがないと全部1行になる）


# def has_tasks(tasks): #「タスクリストが空かどうかをチェックする」もの

#       if not tasks: #「tasksが空なら」 という意味
#             print("タスクがありません") #空ならfalseからtrueになってfalseを返す
#             return False #関数をその場で終了する
      
#       return True # not　は !　と同じ意味

#def is_valid_number(tasks,num): #番号が有効かチェックする

#       return 1 <= num <= len(tasks) 
#       #numが1以上、かつtasksの長さ以下かどうか



