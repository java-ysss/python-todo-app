from task import Task #「task.py の Task クラス使わせて」

class Manager: #タスク全体を管理する

      def __init__(self):
            self.tasks = [] # 最初は空 箱が作られるイメージ


      def load_tasks(self):
            try:
                  with open("tasks.txt","r",encoding = "utf-8")as file:#"r"は読み込む
                        
                        self.tasks = []

                        for line in file: #1行ずつ取り出すって意味
                        
                              name,done = line.strip().split("|") #splitって何？ "勉強|False" を　["勉強", "False"] に分解する .strip()は余計な改行や空白を消す


                              task = Task(name,done == "True")
                              #task = {
                              #      "name" : name,
                              #      "done" : done == "True"
                              #} (辞書)

                              self.tasks.append(task)
                        
            except FileNotFoundError:#初回起動時にはファイルがないから「ファイルないなら空リスト返す」
                  self.tasks = []

    
      def save_tasks(self): #self.tasks をファイルに保存する
            with open("tasks.txt","w",encoding = "utf-8")as file: #下に意味を書いてる

                  for task in self.tasks: #タスクリストを1つずつ取り出す
                        file.write(task.name + "|" + str(task.done) + "\n")


      def add_task(self,name): #リストの末尾に要素を追加するメソッド
        
            task= Task(name)
            self.tasks.append(task)
            self.save_tasks()
        
        #tasks.append(new_task)  #tasks というリストの末尾に new_task を追加するという意味
        #new_task = {
            #  "name" : task,
            #  "done" : False #タスクを追加した瞬間は、まだ何もやっていないからfalse
        #} {} は辞書

      
      def delete_task(self,num):

            if 1 <= num <= len(self.tasks):
                  self.tasks.pop(num - 1)
                  self.save_tasks()
            else:
                  print("その番号はありません")


      def edit_task(self,num,new_name): #「指定した番号のタスク名を書き換えて、保存する」メソッド
            
            if 1 <= num <= len(self.tasks): #有効な範囲内かチェックしている
                  self.tasks[num - 1].name = new_name #Taskオブジェクトの name を変更してる
                  self.save_tasks()
            else:
                  print("その番号はありません")


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


      def delete_done_tasks(self):
      
            self.tasks[:] = [task for task in self.tasks if not task.done] #「未完了だけ残す」➀

            self.save_tasks()
            print("完了済みタスクを削除しました")


      

      def show_tasks(self):
        
            if not self.tasks:
                  print("タスクがありません")
                  return
            
            self.display_tasks()


      def display_tasks(self):# タスクリストを整形して表示する関数 「ToDoリストを見やすく表示する関数」
      
            for i, task in enumerate(self.tasks,start=1):

                  print(i,task) 
      
      
     


#===============================================================
#manager = Manager() 「Managerクラスから、Managerオブジェクト（実体）を作って、manager に入れてる」

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