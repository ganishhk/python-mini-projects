class bankaccount:
    def __init__(self,account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def money_withdraw(self,withdraw):
        if withdraw > 0:
            if self.balance < withdraw:
                print("Insufficient balance")
            else:
                self.balance=self.balance-withdraw
                print(f"money withdraw ₹{withdraw} successfully\n updated balance {self.balance}")
        elif withdraw < 0:
            print("you cant enter negitive number !!")

    def deposit_money(self,deposit):
        if deposit > 0 :
            self.balance=self.balance+deposit
            print(f"money deposit : {deposit} \n updated balance : {self.balance}")
        elif deposit < 0:
            print("you can not deposit negitiive amount !!")

    def show_balance(self):
        print(f"account holder : {self.account_holder}")
        print(f"balance : ₹{self.balance}")

    def tranfer_money(self,account,amount):
        if self.balance < amount:
            print("Insufficient balance cant transfer !!")
        else :
            account.deposit_money(amount)
            self.balance = self.balance - amount
            print(f"money debited {amount} aman balance {self.balance}")
            print(f"tranfer money {amount} to {account}")
        


# example
# ganish = bankaccount("ganish",2500000000)
# aman = bankaccount("aman",250000)
# aman.tranfer_money(ganish, 5000)
# ganish.show_balance()
# aman.show_balance()
# ganish.money_withdraw(-5000)
# ganish.deposit_money(10000)

