'''
Exercise: 6 points

Fill out the missing parts in the code below (5 points)

HINTS:

* You will have to replace the 'pass' statements with some
  meaningful code. Pay attention to the comments which
  describe what is expected.

* You may want to comment out parts of the main application
  while coding! If you just run this, you will get errors at first!


'''

#######################################
# CLASSES FOR THE BANKING APPLICATION #
#######################################


class Customer:
    ''' objects of this class represent customers.
    The customer ID is supposed to be assigned automatically
    when a new customer object is created.
    Attributes:
    - first name
    - last name
    - age
    '''
    customerID = 0
    
    # CONSTRUCTOR
    def __init__(self, fn, ln, age):
        self.cust_id = Customer.customerID
        self.fn = fn
        self.ln = ln
        self.age = age
        Customer.customerID += 1

    # INSTANCE METHODS
    def increment_age(self):
        ''' increases the age by 1 year '''
        self.age += 1

    def __str__(self):
        return "Name: " + self.fn + " " + self.ln + "\tAge: " + str(self.age)

    # SETTERS
    def set_firstname(self, fn):
        ''' sets the first name of a customer '''
        self.fn = fn

    def set_lastname(self, ln):
        ''' sets the last name of a customer '''
        self.ln = ln

    def set_age(self, age):
        ''' sets the age of a customer '''
        self.age = age

    # STATIC METHODS
    ''' write a method called print_info here that prints
    out how many customers have been created so far '''
    @staticmethod
    def print_info():
        print(Customer.customerID, "customers have been created.")


class Account:
    ''' Objects created from this class
    represent accounts.
    Account ID is assigned automatically when creating
    an account object.
    Attributes:
    - number
    - holder (object of class 'Customer')
    - balance '''
    accountID = 0
    
    # CONSTRUCTOR
    def __init__(self, holder):
        ''' the initialization method is called right after
        an object has been created. used to initialize attributes'''
        self.acc_id = Account.accountID
        Account.accountID += 1
        self.holder = holder
        self.balance = 0

    # INSTANCE METHODS
    def withdraw(self, amount):
        ''' withdraw an amount of money from an account object:
        subtract the amoun from the balance, does not allow a
        negative balance. Returns the amount that was actually
        withdrawn from the account. '''
        if amount > self.balance:
            amount = self.balance
        self.balance -= amount
        return amount
        
    def deposit(self, amount):
        ''' deposit an amount of money into an account:
        add the amount of money to the balance '''
        self.balance += amount

    def set_holder(self, new_holder):
        ''' change the account holder.
        We could validate, whether new_holder is 
        a Customer object, as required. '''
        self.holder = new_holder
        
    def __str__(self):
        ''' returns a string describing the account object '''
        return "[Account: ID=" + str(self.acc_id) \
              + " BALANCE=$" + str(self.balance) \
              + " HOLDER=" + str(self.holder)+ "]"


class Bank:
    ''' class for objects that represent a bank
    Attributes:
    - name
    - accounts (dictionary, listed by account ID)
    - customers (dictionary, listed by customer ID) '''
    # CONSTRUCTOR
    def __init__(self, name):
        # list accounts by account ID
        # list customers by ID
        self.name = name
        self.accounts = {}
        self.customers = {}

    # INSTANCE METHODS
    def print_accounts(self):
        ''' print out all accounts of the bank '''
        print("\n** ACCOUNTS **")
        for account in self.accounts.values():
            print(account)

    def print_customers(self):
        ''' prints out all the customers of the bank '''
        print("\n** CUSTOMERS **")
        for customer in self.customers.values():
            print(customer)

    def add_customer(self, customer):
        ''' adds a customer object to the bank's customers '''
        self.customers[customer.cust_id] = customer

    def add_account(self, account):
        ''' adds an account object to the bank's accounts '''
        self.accounts[account.acc_id] = account

    def deposit(self, acc_id, amount):
        ''' deposit money into the account '''
        self.accounts[acc_id].deposit(amount)

    def withdraw(self, cust_id, acc_id, amount):
        ''' withdraw money from the account with the given ID,
        but only if its holder has the given customer ID.
        Returns the amount of money (=cash)'''
        account = self.accounts[acc_id]
        withdrew = 0
        if account.holder.cust_id == cust_id:
            withdrew = account.withdraw(amount)
        return withdrew

    def __str__(self):
        ''' returns a descriptive string for the bank '''
        result = "Bank name: " + self.name + "\nCustomers: " + str(len(self.customers)) + "\nAccounts: " + str(len(self.accounts))
        return result


##############################
# BANKING APPLICATION - MAIN #
##############################

if __name__ == "__main__":
    # Create a new bank object
    bank = Bank("PYTHON-BANK")
    print(bank)

    # Create a few customers and add them to the bank object
    marc = Customer("Marc", "Schulder", 85)
    bank.add_customer(marc)
    stefan = Customer("Stefan", "Thater", 76)
    bank.add_customer(stefan)
    maja = Customer("Maja", "Biene", 2)
    bank.add_customer(maja)

    # Print out all the customers of the bank
    bank.print_customers()
    
    # Create a few accounts and add them to the bank object
    marcsAcc1 = Account(marc)
    bank.add_account(marcsAcc1)
    marcsAcc2 = Account(marc)
    bank.add_account(marcsAcc2)
    stefansAcc = Account(stefan)
    bank.add_account(stefansAcc)
    majasAcc = Account(maja)
    bank.add_account(majasAcc)

    # Print out all the accounts of the bank
    bank.print_accounts()

    # Deposit money into accounts
    print("\nMarc deposits $400 into account with ID 1.")
    bank.deposit(1, 400)
    print("Stefan's customer ID:", stefan.cust_id)
    print("Stefan deposits $1000 into account with ID 2.")
    bank.deposit(2, 1000)

    # Print out all the accounts of the bank
    bank.print_accounts()

    # Withdraw money from some accounts
    print("\nMarc tries to withdraw from Stefan's account.")
    cash = bank.withdraw(0, 2, 100)
    print("Marc got:", cash)
    print("Now Marc tries to withdraw from his own account.")
    cash = bank.withdraw(0,1,100)
    print("Marc got:", cash)

    # Number of customers
    print("")
    Customer.print_info()
    print("Number of customers that have been added to the bank:", len(bank.customers.keys()))   
    
