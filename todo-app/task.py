class Task:

    def __init__(self,name,done = False): #initは何？ javaでいうコンストラクタ
        
        self.name = name # self は this みたいなもの
        self.done = done #渡された値を使う


    def toggle_done(self): #タスクの完了状態をON/OFFするボタン」のようなメソッド
        self.done = not self.done



#======================================-

#self はクラスのメソッドには必ず第1引数に書くルールがある
#__str__ は「このオブジェクトを文字列で表すとどうなるか」を定義するメソッド
#__init__ や __str__ のように __ で囲まれたメソッドはPythonでは特殊メソッドと呼ばれていて、
# Pythonが自動で呼び出してくれる特別なもの