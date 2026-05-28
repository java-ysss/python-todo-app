class Task:

    def __init__(self,name,done = False,priority = None,deadline = None): #initは何？ javaでいうコンストラクタ
        
        self.name = name # self は this みたいなもの
        self.done = done #渡された値を使うからdone
        self.priority = priority
        self.deadline = deadline


    def toggle_done(self): #タスクの完了状態をON/OFFするボタン」のようなメソッド
        self.done = not self.done

    def __str__(self):#➁
        status = "[x]" if self.done else "[ ]" # ➂ 条件がTrueなら左、Falseなら右 という構造
        
        priority_label = {1: "高", 2: "中" ,3: "低"}

        #self.priorityが１なら"高"が取れる

        if self.priority is None:
            label = ""
        else:
            label = f"(優先度: {priority_label[self.priority]})"

        if self.deadline is None:
            deadline_label = ""
        else:
            deadline_label = f"(期限: {self.deadline})"
        

        return f"{status} {self.name} {label} {deadline_label}" #➀
    
    def to_dict(self): #Taskオブジェクトを変換するための機能。
        return{
            "name" : self.name,
            "done" : self.done,
            "priority" : self.priority,
            "deadline" : self.deadline
        }

#======================================-

#self はクラスのメソッドには必ず第1引数に書くルールがある
#__str__ は「このオブジェクトを文字列で表すとどうなるか」を定義するメソッド
#__init__ や __str__ のように __ で囲まれたメソッドはPythonでは特殊メソッドと呼ばれていて、
# Pythonが自動で呼び出してくれる特別なもの

#　➀　f文字列（f-string）の説明  / 　f"文字列{変数}文字列"　
# f を頭につけると、{}の中に変数を埋め込める文字列になる
# ➁　__str__ メソッドとは
# オブジェクトを文字列として表示するときの見た目を定義するメソッド

#➂ if self.done:
#       status = "[x]"
#   else:
#       status = "[]" 一行にしないとこんな感じの式になる

