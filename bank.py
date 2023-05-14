class Atm:
    #property
    #behaviour
    #pin
    #balance

    #withdraw
    #check balance
    #deposit
    #create pin
    #change pin
    #Receipt ->last 5 Transaction


    
    def create_pin(self):
       user_pin = input("enter pin of 4 digit between 1000 and 9999")
       confirm_pin = input("type again")

       if self.pin == user_pin:
            self.balance=0
            print("print created")
        
            
                                 
    def change_pin(self):
        old_pin = input("enter old pin")
        if self.pin == old_pin:
            self.create_pin()
        else:
                 print("pin does not match")
        
    def withdraw(self):
        user_input = input("enter pin")
        if self.pin == user_input:
            amount = (int(input("enter the amount")))
            if amount <=self.balance:
                         self.balance = self.balance-amount
                         print("Transaction Succesful")
            else:
                              print("fakir")
        else:
                          print("phir se dal")
    def deposit(self):
            user_input = input("enter pin")
            if self.pin == user_input:
                amount = (int(input("Kitna Beta?")))
                self.balance =  self.balance +amount
                print("deposit done")
            else:
                                print("Try Again")
        
    def check_balance(self):
        user_input = input("enter pin")
        if self.pin == user_input:
            print("balance->" .self.balance)
        else:
                print("incorrect pin")
