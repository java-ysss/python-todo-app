class Task:

    def __init__(self,name,done = False): #initは何？ javaでいうコンストラクタ
        
        self.name = name # self は this みたいなもの
        self.done = done #渡された値を使うからdone


    def toggle_done(self): #タスクの完了状態をON/OFFするボタン」のようなメソッド
        self.done = not self.done

    def __str__(self):#➁
        status = "[x]" if self.done else "[ ]" # ➂ 条件がTrueなら左、Falseなら右 という構造
        return f"{status}{self.name}" #➀

#======================================-

#self はクラスのメソッドには必ず第1引数に書くルールがある
#__str__ は「このオブジェクトを文字列で表すとどうなるか」を定義するメソッド
#__init__ や __str__ のように __ で囲まれたメソッドはPythonでは特殊メソッドと呼ばれていて、
# Pythonが自動で呼び出してくれる特別なもの

#　➀　f文字列（f-string）の説明  / [　f"文字列{変数}文字列"　]
# f を頭につけると、{}の中に変数を埋め込める文字列になる
# ➁　__str__ メソッドとは
# オブジェクトを文字列として表示するときの見た目を定義するメソッド

#➂ if self.done:
#       status = "[x]"
#   else:
#       status = "[]" 一行にしないとこんな感じの式になる


