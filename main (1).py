#Simple Bank System
#Parent class/classe Pai   - (Python Object Oriented)
class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name",self.name)
        print("Age",self.age)
        print("Gender",self.gender)
        
#Child Class/ Classe filha- Esta classe herda características da Classe Pai
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
        
    #função depósito
    def deposit(self,amount):
        self.amount=amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: €",self.balance)
        
     #função saque   
    def withdraw(self,amount):
        self.amount=amount
        #se o valor em caixa for insuficiente
        if self.amount> self.balance:
            print("Insufficient Fund|Balance Available : €",self.balance)
        #caso contrário
        else:
            self.balance=self.balance-self.amount
            print("Account balance has been updated: €",self.balance)
            
    def view_balance(self):
        self.show_details()
        print("Account balance: €",self.balance)
        
        
#Example
iara=Bank("Iara",35,"Female")
Henrique=Bank("Henrique",34,"Male")

iara.deposit(1000)


iara.withdraw(500)


iara.show_details()
iara.view_balance()

    