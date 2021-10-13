class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.balance < amount:
            self.balance -= 5
            return ('Insufficient funds: Charging a $5 fee')

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, username, email_address, int_rate, amount):
        self.username = username
        self.email = email_address
        self.account = BankAccount(int_rate, amount)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
            self.account.make_withdrawal(amount)
            return self

    def display_user_balance(self):
        print(f"{self.username}'s current account balance is ${self.account.display_account_info()}.")
        return self

    def transfer_money(self, other_user, amount):
        other_user.account.deposit(amount)
        self.account.make_withdrawal(amount)
        return self
    
    def monthly_interest(self):
        self.account.yield_interest()
        return self

    # def __repr__(self):
    #     print(f"Int Rate: {self.int_rate}%  Balance: ${self.balance}")
    #     return f"Int Rate: {self.int_rate}%  Balance: ${self.balance}"    
    # #tim thought this would take away <__main__.User object at 0x000002315D7D9FD0> that is printing in the output.



anna = User("anna", "anna.Frank@gmail.com", 1, 100000)
michael = User("Mike", "Mike.Todd@gmail.com", 2, 500000)

michael.make_deposit(100).make_deposit(200).make_withdrawal(1000).make_deposit(200)

anna.make_deposit(1000).make_withdrawal(2000).make_deposit(2000).make_withdrawal(2000).make_withdrawal(100).make_withdrawal(200).transfer_money(michael, 500)

print(anna.display_user_balance())


##class RetirementAccount(BankAccount):
    # def __init__(self, int_rate, is_roth, balance=0):
    # 	super().__init__(int_rate, balance)	
    #     self.is_roth = is_roth	

    ##class BankAccount:
    # def __init__(self, int_rate, balance=0):
    #     self.int_rate = int_rate
    #     self.balance = balance


    # class RetirementAccount(BankAccount):
    # def withdraw(self, amount, is_early):
    # 	if is_early:
    # 	    amount = amount * 1.10
    # 	if (self.balance - amount) > 0:
    # 	    self.balance -= amount
    #     else:
    # 	    print("INSUFFICIENT FUNDS")
    # 	return self


# class BankAccount:
#     def withdraw(self, amount):
#     	if (self.balance - amount) > 0:
#     	    self.balance -= amount
#         else:
#     	    print("INSUFFICIENT FUNDS")
#     	return self
    
#Hopefully you recognize the repetitiveness here and want to reduce it! So let's call on the parent to do the part of the code that is the same:
    # class RetirementAccount(BankAccount):
    # def withdraw(self, amount, is_early):
    # 	if is_early:
    # 	    amount = amount * 1.10
    # 	super().withdraw(amount)
    # 	return self

    # class BankAccount:
    # def withdraw(self, amount):
    # 	if (self.balance - amount) > 0:
    # 	    self.balance -= amount
    #     else:
    # 	    print("INSUFFICIENT FUNDS")
    # 	return self


    


    






