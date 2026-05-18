

def save_tasks(tasks): #タスクのリストを受け取る関数を定義
      with open("tasks.txt","w",encoding = "utf-8")as file: #下に意味を書いてる

        for task in tasks: #タスクリストを1つずつ取り出す
              file.write(task["name"] + "|" + str(task["done"]) + "\n")

def load_tasks():
      try:
            with open("tasks.txt","r",encoding = "utf-8")as file:#"r"は読み込む
                  
                  tasks = []

                  for line in file: #1行ずつ取り出すって意味
                        
                        name,done = line.strip().split("|") #splitって何？ "勉強|False" を　["勉強", "False"] に分解する

                        task = {
                              "name" : name,
                              "done" : done == "True"
                        }

                        tasks.append(task)

                  return tasks
        #tasks.append(line.strip())#.strip()は余計な改行や空白を消す
      except FileNotFoundError:#初回起動時にはファイルがないから「ファイルないなら空リスト返す」
            return []

def input_task():

        while True:
            
            task = input("タスク名 > ").strip() #空白だけ入力も防げる。

            if task: #空文字 → False 文字あり → True
                return task
            
            print("空入力できません")

    #関数の結果を外で使いたい？
    #YES → return 必要
    #NO → return なくてもOK

def show_tasks(tasks):
        
        if not tasks:
            print("タスクがありません")
        else:
            display_tasks(tasks)

def add_task(tasks,task): #リストの末尾に要素を追加するメソッド
        
        new_task = {
              "name" : task,
              "done" : False #タスクを追加した瞬間は、まだ何もやっていないからfalse
        }
        tasks.append(new_task) #{}は辞書

def delete_task(tasks):
        
      display_tasks(tasks)

      delete_num = input_number("削除番号 > ")

      if is_valid_number(tasks,delete_num):

            tasks.pop(delete_num - 1)  #pop()は、リストから要素を取り出して削除するメソッド
      else:
            print("その番号はありません")

def edit_task(tasks):
      
      if not has_tasks(tasks):
            return
      display_tasks(tasks)

      
      edit_num = input_number("編集番号 >")

      if is_valid_number(tasks,edit_num):

            new_task = input("新しいタスク名 > ")

            tasks[edit_num - 1]["name"] = new_task #「リストの特定位置を操作する」
      else:
            print("その番号はありません")

      
def toggle_task(tasks):
      
            if not has_tasks(tasks):
                  return
            
            display_tasks(tasks)

            
            toggle_num = input_number("完了切り替え番号 > ")

            if is_valid_number(tasks,toggle_num):
                        
                  task = tasks[toggle_num - 1]

                  task["done"] = not task["done"] #今の状態(右側)を反転してもう一回代入してる

            else:
                  print("その番号はありません")
                


def delete_done_tasks(tasks):
      
      tasks[:] = [task for task in tasks if not task["done"]] #「未完了だけ残す」

      print("完了済みタスクを削除しました")


def display_tasks(tasks):# タスクリストを整形して表示する関数 「ToDoリストを見やすく表示する関数」
      
      for i, task in enumerate(tasks,start=1):
            
            status = "[x]" if task["done"] else "[ ]"#条件がTrueなら左、Falseなら右 という構造

            print(i,status,task["name"]) #「番号、チェックボックス、タスク名」を左から並べてるだけ
    

def has_tasks(tasks): #「タスクリストが空かどうかをチェックする」もの

      if not tasks: #「tasksが空なら」 という意味
            print("タスクがありません") #空ならfalseからtrueになってfalseを返す
            return False #関数をその場で終了する
      
      return True # not　は !　と同じ意味

def input_number(message):#番号入力関数

      while True:

            try:
                  return int(input(message))

            except ValueError:
                  print("数字を入力してください")


def is_valid_number(tasks,num): #番号が有効かチェックする

      return 1 <= num <= len(tasks) 
      #numが1以上、かつtasksの長さ以下かどうか


#==============================================================--



def main():
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
                add_task(tasks,task)
                save_tasks(tasks)

            elif choice == "2":
                show_tasks(tasks)

            elif choice == "3":
                delete_task(tasks)
                save_tasks(tasks)

            elif choice == "4":

                edit_task(tasks)
                save_tasks(tasks)


            elif choice == "5":
                  
                  toggle_task(tasks)
                  save_tasks(tasks)


            elif choice == "6":
                 
                delete_done_tasks(tasks)
                save_tasks(tasks)

            elif choice == "7":
                save_tasks(tasks)

                break

tasks = load_tasks()
main()


#withは「後片付けを自動化する仕組み」って考えるとかなり理解しやすい。
# with open("tasks.txt","w",encoding = "utf-8")as file:
#open("tasks.txt")  tasks.txt というファイルを開く（なければ新規作成）
# "w"  書き込みモード（上書き）
# encoding="utf-8" 日本語が文字化けしないようにする
# as file  開いたファイルを file という名前で使う
# with  処理が終わったら自動でファイルを閉じてくれる
#file.write()  ファイルに文字を書き込む
# { + "\n" }  改行を追加（これがないと全部1行になる）

