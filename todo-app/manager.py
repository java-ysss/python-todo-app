import os
import json #責任の分離 「どう保存するか」はManagerの仕事
from datetime import date #日付モジュール

#today = date.today() #今日の日付 クラスの外に置かないほうがいい

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR,"tasks.json")
from task import Task #「task.py の Task クラス使わせて」

class Manager: #タスク全体を管理する

      def __init__(self): # __init__ は　「オブジェクトが作られた瞬間に自動で実行される初期化処理」
            self.tasks = [] # 最初は空 箱が作られるイメージ


      def load_tasks(self):
            try:
                  with open(FILE_PATH,"r",encoding = "utf-8")as file:#"r"は読み込む
                  
                       data = json.load(file) #ファイルの中身をPythonのリストとして読み込む。
                       self.tasks = [Task(d["name"],d["done"],d["priority"],d["deadline"]) for d in data] #dataのリストを1つずつ取り出して、Taskオブジェクトに変換する
                        
            except FileNotFoundError:#初回起動時にはファイルがないから「ファイルないなら空リスト返す」
                  self.tasks = []

    
      def save_tasks(self): #self.tasks をファイルに保存する
            
            with open(FILE_PATH,"w",encoding = "utf-8")as file: #下に意味を書いてる

                  data = [task.to_dict() for task in self.tasks] #[ 作る値 for 取り出す変数 in リスト ] ➄
                  json.dump(data,file,ensure_ascii=False,indent=2) #dump は 「データをファイルに書き出す（吐き出す）」 という意味

                  # for task in self.tasks: #タスクリストを1つずつ取り出す
                  #       file.write(task.name + "|" + str(task.done) + "\n")


      def add_task(self,name,priority,deadline): #リストの末尾に要素を追加するメソッド
        
            task = Task(name,priority=priority,deadline=deadline) # priority = priority をキーワード引数といいます。順番に関係なく名前で指定できるので、今回みたいに間に別の引数がある場合に使います。
            self.tasks.append(task) #appendは一つしか引数を受け取れない
            self.save_tasks()
        
        #tasks.append(new_task)  #tasks というリストの末尾に new_task を追加するという意味
        #new_task = {
            #  "name" : task,
            #  "done" : False #タスクを追加した瞬間は、まだ何もやっていないからfalse
        #} {} は辞書

      def edit_task(self,num,new_name): #「指定した番号のタスク名を書き換えて、保存する」メソッド
            
            if 1 <= num <= len(self.tasks): #有効な範囲内かチェックしている
                  self.tasks[num - 1].name = new_name #Taskオブジェクトの name を変更してる
                  self.save_tasks()
            else:
                  print("その番号はありません")

      def edit_menu(self):  #「どのタスクを編集するか選んで、新しい名前を入力させる」
            
            if not self.tasks:
                  print("タスクがありません")
                  return
            
            self.show_tasks()

            while True:
                  try:
                        num = int(input("編集番号 > "))

                        if 1 <= num <= len(self.tasks):
                              break
                        else:
                              print("その番号はありません")

                  except ValueError:
                        print("数字を入力してください")
            
            while True:
                  new_name = input("新しいタスク名 > ").strip() #.strip() で前後の空白を除去 空文字もはじける

                  if new_name:
                        break
                  print("空入力できません")

            self.edit_task(num,new_name)



      def toggle_task(self,num): #タスクの「完了 / 未完了」を切り替える関数
      
            if not self.tasks: #空チェック
                  print("タスクがありません")
                  return
            
            if 1 <= num <= len(self.tasks):
                  
                  task = self.tasks[num - 1]
                  task.toggle_done() #Task クラスに仕事を任せる
                  self.save_tasks() #txtに反映

            else:
                  print("その番号はありません")
            #task.done = not task.done #今の状態(右側)を反転してもう一回代入してる


      def delete_done_tasks(self): #完了済みタスクを削除する メソッド
            
            before = len(self.tasks) #削除前のタスクの数を before に保存しておく

            self.tasks[:] = [task for task in self.tasks if not task.done] #「未完了だけ残す」➀

            after = len(self.tasks) #削除後のタスクの数を after に保存

            if before == after: #削除前と削除後の数が同じ＝完了済みタスクが1つもなかった
                  print("削除する完了済みのタスクがありません")
                  return

            self.save_tasks()
            print("完了済みタスクを削除しました")


      def show_tasks(self): # タスクリストを整形して表示する関数 「ToDoリストを見やすく表示する関数」
        
            if not self.tasks:
                  print("タスクがありません")
                  return
            print("======= TASK LIST ========")

            for i, task in enumerate(self.tasks,start=1):

                  print(i,task) 
            print("======= TASK LIST ========")


      def show_tasks_by_priority(self): #優先度順に並べるメソッド
            self.tasks.sort(key=lambda task: task.priority or 99) #➅
            #sort(key=...) は「何を基準に並び替えるか」を指定します。

            print("======= TASK LIST ========")

            for i, task in enumerate(self.tasks,start=1):

                  print(i,task) 
            print("======= TASK LIST ========")
           


      def search_tasks(self,keyword): #keyword は検索したい文字
            found = False

            for task in self.tasks:
                  if keyword in task.name: #取り出した task の name（名前）に、keyword が含まれているかを確認します。
                        print(task)
                        found = True

            if not found:
                  print("見つかりませんでした")


      def show_undone_tasks(self): #未完了だけ表示するメソッド

            print("=== 未完了 ===")

            for i, task in enumerate(self.tasks,start=1):
                  if not task.done:
                        print(i,task)

      def show_done_tasks(self): #完了済みだけ表示

            print("=== 完了済み ===")

            for i, task in enumerate(self.tasks,start=1):
                  if task.done:
                        print(i,task)


      def show_summary(self):
            total = len(self.tasks) # len ()要素の数をいくつあるか返してくれる
            done_count = sum(1 for task in self.tasks if task.done) #sum() はリストの合計を出す組み込み関数
 
            undone_count = total - done_count

            print(f"全部 : {total}")
            print(f"完了 : {done_count}")
            print(f"未完了 : {undone_count}")
                  

      def delete_menu(self): #「削除メニュー」のメソッドの定義

            if not self.tasks:
                  print("タスクがありません")
                  return
            
            self.show_tasks()

            while True:
                  try:
                        num = int(input("削除番号 > ")) #ユーザーに削除したい番号を入力してもらい、int で数字に変換

                        if 1 <= num <= len(self.tasks):
                              self.delete_task(num) #入力された番号のタスクを削除
                              break #削除が成功したらループを終了
                        
                  except ValueError:
                        print("数字を入力してください")

      def show_deadline_tasks(self):
            today = date.today() #今日の日付を date 型で取得して today に入れる。
            found = False #締め切りが近いタスクが1つも見つかっていない」状態をフラグで管理。最初は False

            print("=== 締め切りが近いタスク (7日以内) ===")

            for i,task in enumerate(self.tasks,start=1):

                  if task.deadline is None: #期限なしはスキップ
                        continue #「次のループへ飛ぶ」

                  task_deadline = date.fromisoformat(task.deadline) #文字列 →　date型に変換
                                    #fromisoformat は ISO形式（YYYY-MM-DD）の文字列を date に変換するメソッド
                  
                  diff = (task_deadline - today).days #今日から何日後か
                  #締め切り日から今日を引いて、何日後かを整数で取得。date 型同士の引き算は timedelta 型になるので、.days で日数だけ取り出す
                  #print(f"デバック : {task.name} diff = {diff}")
                  if 0 <= diff <= 7: #今日～７日以内
                        print(i,task)
                        found = True #found = True で「1件見つかった」と記録。

                  elif diff < 0: #期限切れ
                        print(f"期限切れ({abs(diff)}日経過)",task) #diff がマイナス = 締め切りが過ぎている。abs() は絶対値（マイナスを取り除く）なので、-3 → 3 になり「3日経過」と表示できる。
                        found = True

            if not found:
                  print("締め切りが近いタスクはありません")
      



      
      
      
     


#===============================================================

#len() は　() の中に入れたものが いくつあるか を数えてくれます。

#main は入力.表示　Manager　タスク管理 　Task　1個のタスクの状態管理

#➀　# 普通のforループ版
# new_tasks = []
# for task in self.tasks:
#     if not task.done:
#         new_tasks.append(task)
# self.tasks[:] = new_tasks

# # ↓ これを1行にまとめたのがリスト内包表記
# self.tasks[:] = [task for task in self.tasks if not task.done]

# self.tasks = [...]    # tasksを新しいリストに差し替え
# self.tasks[:] = [...] # tasksの中身だけを入れ替え（箱はそのまま）


      #def delete_task(self,num): #指定した番号のタスクを削除するメソッド

      #       if 1 <= num <= len(self.tasks):
      #             self.tasks.pop(num - 1) #該当のタスクをリストから取り除く
      #             self.save_tasks()
      #       else:
      #             print("その番号はありません")

#sum(1 for task in self.tasks if task.done)
#   ↑ 条件を満たすたびに1を出す
#                              ↑ doneがTrueのときだけ
# → 1が何個出たか = 完了タスクの数  完了タスクを1個見つけるたびに「1」と書いた紙を積み上げて、最後に枚数を数える感じです。

# ➄ data = []

# for task in self.tasks:

#     dic = {
#         "name": task.name,
#         "done": task.done
#     }

#     data.append(dic)

#➅ # lambda task: task.priority or 99 は：
      # self.tasks の中から task を1つずつ取り出して
      # その task.priority の値を返す
      # None のときは 99 を返す（一番後ろにしたいから）


