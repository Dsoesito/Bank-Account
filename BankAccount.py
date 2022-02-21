class Account:
    
    def __init__(self, user_id, checking_bal, savings_bal, business_bal):
        self.user_id = user_id
        self.checking_bal = abs(checking_bal)
        self.savings_bal = abs(savings_bal)
        self.business_bal = abs(business_bal)
    
    # CHECKING ACCOUNT        
    def checking_deposit(self, deposit_amount): # deposit to checking
        
        if deposit_amount <= 0: #check deposit to be more than zero
            print("Please deposit a positive amount!")
            
        else:
            self.checking_bal += deposit_amount
            print("$", deposit_amount, "has been deposited in", self.user_id, "checking account.")
        
    def checking_withdraw(self, withdraw_amount): # withdraw from checking
        
        if withdraw_amount <= 0:
            print("Please withdraw a positive amount!") # check for positive withdraw
        
        elif withdraw_amount > self.checking_bal: #check withdrawl to be less than balance
            print("Please lower withdrawl!")
        
        else:
            self.checking_bal -= withdraw_amount
            print("$", withdraw_amount, "has been withdrawn from", self.user_id, "checking account.")
        
    def checking_to_savings(self, transfer_amount): # transfer from checking to savings
        
        if transfer_amount <= 0: # check for positive transfer
            print("Please transfer a positive amount!")
        
        elif transfer_amount > self.checking_bal: #check transfer to be less than balance
            print("Please lower transfer amount!")
            
        else:
            self.checking_bal -= transfer_amount
            self.savings_bal += transfer_amount
            print("$", transfer_amount, "has been transfered from checking to savings.")
            
    def checking_to_business(self, transfer_amount): # transfer from checkign to business
        
        if transfer_amount <= 0: # check for positive transfer
            print("Please transfer a positive amount!")
        
        elif transfer_amount > self.checking_bal: #check transfer to be less than balance
            print("Please lower transfer amount!")
            
        else:
            self.checking_bal -= transfer_amount
            self.business_bal += transfer_amount
            print("$", transfer_amount, "has been transfered from checking to business.")
    
    # SAVIGNS ACCOUNT
    def savings_deposit(self, deposit_amount): #check to be more than zero
        
        if deposit_amount <= 0: #check deposit to be more than zero
            print("Please deposit a positive amount!")
        
        else:
            self.savings_bal += deposit_amount
            print("$", deposit_amount, "has been deposited in", self.user_id, "savings account.")
        
    def savings_withdraw(self, withdraw_amount): #check to be less than balance
        
        if withdraw_amount <= 0: #xcheck for positive withdraw
            print("Please withdraw a positive amount!")
        
        elif withdraw_amount > self.savings_bal: #check withdrawl to be less than balance
            print("Please lower withdrawl!")
        
        else:
            self.savings_bal -= withdraw_amount
            print("$", withdraw_amount, "has been withdrawn from", self.user_id, "savings account.")
        
    def savings_to_checking(self, transfer_amount): # transfer from savings to checking
        
        if transfer_amount <= 0: # check for positive transfer
            print("Please transfer a positive amount!")
        
        elif transfer_amount > self.savings_bal: # check transfer to be less than balance
            print("Please lower transfer amount!")
            
        else:
            self.savings_bal -= transfer_amount
            self.checking_bal += transfer_amount
            print("$", transfer_amount, "has been transfered from savings to checking.")
            
    def savings_to_business(self, transfer_amount): # transfer from savings to business
        
        if transfer_amount <= 0: # check for positive transfer
            print("Please transfer a positive amount!")
        
        elif transfer_amount > self.savings_bal: # check transfer to be less than balance
            print("Please lower transfer amount!")
            
        else:
            self.savings_bal -= transfer_amount
            self.business_bal += transfer_amount
            print("$", transfer_amount, "has been transfered from savings to business.")
    
    # BUSINESS ACCOUNT    
    def business_deposit(self, deposit_amount): #check to be more than zero
        
        if deposit_amount <= 0: #check deposit to be more than zero
            print("Please deposit a positive amount!")
        
        else:
            self.business_bal += deposit_amount
            print("$", deposit_amount, "has been deposited in", self.user_id, "business account.")
        
    def business_withdraw(self, withdraw_amount): #check to be less than balance
        
        if withdraw_amount <= 0: # check for positive withdraw
            print("Please withdraw a positive amount!")
        
        elif withdraw_amount > self.business_bal: #check withdrawl to be less than balance
            print("Please lower withdrawl!")
        
        else:
            self.business_bal -= withdraw_amount
            print("$", withdraw_amount, "has been withdrawn from", self.user_id, "business account.")
        
    def business_to_savings(self, transfer_amount): # transfer to savings
        
        if transfer_amount <= 0: # check for positive transfer
            print("Please transfer a positive amount!")
        
        elif transfer_amount > self.business_bal: #check transfer to be less than balance
            print("Please lower transfer amount!")
            
        else:
            self.business_bal -= transfer_amount
            self.savings_bal += transfer_amount
            print("$",transfer_amount, "has been transfered from business to savings.")
            
    def business_to_checking(self, transfer_amount): # transfer to business
        
        if transfer_amount <= 0: # check for positive transfer
            print("Please transfer a positive amount!")
        
        elif transfer_amount > self.business_bal: #check transfer to be less than balance
            print("Please lower transfer amount!")
            
        else:
            self.business_bal -= transfer_amount
            self.checking_bal += transfer_amount
            print("$", transfer_amount, "has been transfered from business to checking.")
    

user1 = Account("Daniel", 100, 200, 300)

user1.user_id