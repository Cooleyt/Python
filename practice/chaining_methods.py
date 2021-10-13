class Customer():

    def __init__(self, first_name, last_name, email_address, account):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.account_balance = account

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):  
        self.account_balance -= amount
        return self

    def display_user_balance(self, amount):
        self.display_user_balance = amount
        return self

customer1 = Customer("Guido", "Rossum", "guido@python.com", 50000)
customer2 = Customer("Monty", "Python", "monty@python.com", 20000)
customer3 = Customer("Brady", "Bunch", "brady@python.com", 500000)

customer1.make_deposit(100).make_deposit(200).make_withdrawal(1000).make_deposit(200)  #this is called chaining
customer2.make_deposit(1000).make_withdrawal(2000).make_deposit(2000).make_withdrawal(2000)
customer3.make_deposit(5000).make_withdrawal(5000).make_withdrawal(4000).make_withdrawal(1000)



# print(customer1.first_name, customer1.last_name, customer1.account_balance)  #this print the users name and account balance
# print(customer2.account_balance) #this print the second customers account balance
# print(customer2.first_name, customer2.last_name, customer2.account_balance)
print(customer3.first_name, customer3.last_name, customer3.account_balance)







