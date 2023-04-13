class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance 
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount #self.balance = self.balance + amount
        print(f"{amount} has been deposited into your account")
        
    def withdraw(self, amount):
        self.balance -= amount #self.balance = self.balannce -amount
        if amount > self.balance:
            print("insufficient funds")
            self.balance -= 5
        else: 
            print(f"{amount} has been withdrawn from your account")
            
            
        
        # your code here
    def display_account_info(self):
        # your code here
        print(f"Your current balance is {self.balance}")
        
    def yield_interest(self):
        interest = self.int_rate * self.balance
        self.balance += interest 
        print(f"your current balance with interest is {self.balance}")
        

account1 = BankAccount(0.1, 100)
account2 = BankAccount(0.1,100)
account1.deposit(100)
account1.deposit(100)
account1.deposit(100)
account1.withdraw(100)
account1.yield_interest()
account1.display_account_info()
account2.deposit(100)
account2.deposit(100)
account2.withdraw(100)
account2.yield_interest()
account2.display_account_info()















