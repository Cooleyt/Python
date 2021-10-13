class BankAccount():

    def __init__(self, first_name, last_name, email_address, account, int_rate): 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.account_balance = account
        self.int_rate = int_rate

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.account_balance < amount:
            self.account_balance -= 5
            return ('Insufficient funds: Charging a $5 fee')

        self.account_balance -= amount
        return self

    def display_account_info(self):
        self.account_info
        return self

    def yield_interest(self):
        self.account_balance += self.account_balance * self.int_rate
        return self


customer1 = BankAccount("Guido", "Rossum", "guido@python.com", 50000, 0.01)
customer2 = BankAccount("Monty", "Python", "monty@python.com", 20000, 0.01)

customer1.make_deposit(100).make_deposit(200).make_withdrawal(1000).make_deposit(200)  #this is called chaining
customer2.make_deposit(1000).make_withdrawal(2000).make_deposit(2000).make_withdrawal(2000).make_withdrawal(100).make_withdrawal(200)
print(customer1.yield_interest())
print(customer1.first_name, customer1.last_name, customer1.account_balance, customer1.int_rate)
print(customer2.first_name, customer2.last_name, customer2.account_balance, customer2.int_rate)