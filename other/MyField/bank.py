class BankAccount:
    def __init__(self, owner, __balance=0):
        self.__balance = __balance
        self.owner = owner
    
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Мало бабла')
        else:
            self.__balance -= amount
        
    def get_balance(self):
        return self.__balance
    







