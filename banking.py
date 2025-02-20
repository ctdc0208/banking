# 1. Implement the Account entity class with the following attributes: account_id,
# customer_id, account_number, balance.
#       It should have the following methods: deposit(), withdraw(), and get_balance().
class Account:
    def __init__(self, account_id, customer_id, account_number, balance):
        self.account_id = account_id
        Customer.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"Deposited {amount}")
 
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        print(f"Withdrew {amount}")
    
    def get_balance(self):
        return self.balance


# 2. Implement the Customer entity class with the following attributes: customer_id, name,
# email, and phone_number.
class Customer:
    def __init__(self, customer_id, name, email, phone_number):
        Account.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
    

# 3. Implement a Use Case class for creating a new account. It should have a method named
# create_account() that takes customer_id, name, email, and phone_number as input and
# returns an Account object.
class New_Account:
    def __init__(self, new_account):
        self.new_account = new_account

    def create_account(self, customer_id, name, email, phone_number):
        add_customer= {"customer_id": customer_id, "name": name, "email": email, "phone_number": phone_number}

        random_account_id = 101
        random_account_number = 100
        initial_balance = 0
        add_account = {"account_id": random_account_id, "customer_id": customer_id, "account_number": random_account_number, "balance": initial_balance}

        self.new_account.save_account(add_customer, add_account)


# 4. Implement a Use Case class for making a transaction. It should have a method named
# make_transaction() that takes account_id, amount, and transaction_type (either
# 'deposit' or 'withdraw') as input and updates the account balance accordingly.
class Transaction:
    def make_transaction(self, account_id, amount, transaction_type):
        if transaction_type == 'deposit':
            account_id.deposit(amount)
        if transaction_type == 'withdraw':
            account_id.withdraw(amount)

# 5. Implement a Use Case class for generating account statements. It should have a method
# named generate_account_statement() that takes account_id as input and returns a
# statement string containing transaction details for the given account.
class Statement:
    def generate_account_statement(self, account_id):
        
        print(f"Statement for Account ID: {account_id}")


# 6. Implement an Infrastructure class named AccountRepository for persisting and
# retrieving account data. It should have methods like save_account(),
# find_account_by_id(), and find_accounts_by_customer_id().
class AccountRepository:
    def __init__(self):
        self.accounts = []
        self.customers = []
    
    def save_account(self, customer, account):
        self.customers.append(customer)
        self.accounts.append(account)
        print(f"Account for {customer['name']} added successfully.")
    
    def find_account_by_id(self, account_id):
        for account in self.accounts:
            if account['account_id'] == account_id:
                print(f"For Account ID: {account['account_id']}")
                print(f"Account ID: {account['account_id']},\nCustomer ID: {account['customer_id']},\nAccount Number: {account['account_number']}\n")

    def find_accounts_by_customer_id(self, customer_id):
        customer_accounts = [account for account in self.accounts if account['customer_id'] == customer_id]
        print(f"For Customer ID: {customer_id}")
        for account in customer_accounts:
            print(f"Account ID: {account['account_id']},\nCustomer ID: {account['customer_id']},\nAccount Number: {account['account_number']}\n")


# 7. Implement a simple test scenario that demonstrates the use of all the implemented
# classes and methods.

account_manager = AccountRepository()  
account_creator = New_Account(account_manager)

# Create a few accounts
account_creator.create_account(102, "John Doe", "john.doe@example.com", "+63999")
account_creator.create_account(103, "Jane Smith", "jane.smith@example.com", "+63999")

# test for Transaction
print(f"\nTest for Transaction")
# initial account
account = Account(101, 102, 100, 0)
transaction = Transaction()
print(f"Initial Balance: {account.get_balance()}")
transaction.make_transaction(account, 1000, 'deposit')
print(f"Balance after deposit: {account.get_balance()}")
transaction.make_transaction(account, 500, 'withdraw')
print(f"Balance after withdraw: {account.get_balance()}\n")

# Test for Statement
statement = Statement()
statement.generate_account_statement(account)

# Test for find_account_by_id()
print("For method find_account_by_id()")
account_manager.find_account_by_id(101)

# Test for find_accounts_by_customer_id()
print("For method find_accounts_by_customer_id")
account_manager.find_accounts_by_customer_id(102)



