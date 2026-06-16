
class Customer:

    def __init__(self,id,name,phone,email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"ID : {self.id} 氏名 : {self.name} 番号 : {self.phone} Eメール : {self.email}"
        

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "phone" : self.phone,
            "email" : self.email
        }
    

#=================================

# json.dump() はPythonのオブジェクトをJSONファイルに書き込む関数です。
#流れ Customer → to_dict() → 辞書 → JSON保存 →  〇　→ JSON読込 → 辞書 → Customer() → self.customers
                                                    #「JSONから直接 Customer が出てくる」のではなく、
                                                    #一回辞書になって、それを見ながら Customer を組み立て直している
