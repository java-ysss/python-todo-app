
from customer import Customer
import json

class Customer_Manager:

    def __init__(self):
        self.customers = []
        self.next_id = 1


    def find_customer_by_id(self,id): #IDで顧客を探す処理　一件を返したいときは　変数

        for customer in self.customers:
            if customer.id == id:
                return customer
            
        return None # ← ループが全部終わっても見つからなかった場合

    def add_customer(self,name,phone,email): #追加

        customer = Customer(self.next_id,name,phone,email)

        self.customers.append(customer)
        self.next_id += 1
        

    def show_customer(self): #表示

        if len(self.customers) == 0:
            print("顧客がいません")
            return
        
        for i, customer in enumerate(self.customers,start=1):
            print(i,customer)


    def search_customer(self,name): #検索 複数ある時はリストで返す

        results = [] #空の時がすでにFalse

        for customer in self.customers:
            if customer.name == name:
                results.append(customer)

        return results

    def delete_customer(self,id): #削除

        # if not len(self.customers):
        #     print("削除するものがありません") 責任の分離のため消去
        #     return False

        customer = self.find_customer_by_id(id)
        
        if customer is None:
                return False
                
        self.customers.remove(customer)
        return True
    
        
    
    def edit_customer(self,id,name,phone,email): #編集
        
        customer = self.find_customer_by_id(id)
        
        if customer is None:
            return False
        
        customer.name = name
        customer.phone = phone
        customer.email = email

        return True

        
    def save_customers(self): #保存

        #data = [customer.to_dict() for customer in self.customers] #➀ ↓を簡略化したもの

        data = []

        for customer in self.customers:
            data.append(customer.to_dict())

        with open("customers.json","w",encoding="utf-8")as file:
            json.dump(data,file) #(保存したいもの, 保存先)



    def load_customers(self,file):
        with open("customers.json","r",encoding="utf-8")as file:
            data = json.load(file)

        for item in data:
            customer = Customer(
                item["id"],
                item["name"],
                item["phone"],
                item["email"]
            )
            self.customers.append(customer)

        


#=====================================

# save は オブジェクト → 辞書 → JSON

# load は JSON → 辞書 → オブジェクト


