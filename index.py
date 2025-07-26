#ATM System
class ATM:
    
    #default pin and balance
    def __init__(self): 
        self.pin = 1234
        self.balance = 10000
        self.system()

    #system menu for user to select an option
    def system(self): 
        user_input = int(input("""
        
        =================================            
        Hello, Welcome to the ATM System
        =================================
                               
        Please Select an Option:
        
        1. Check Balance
        2. Withdraw
        3. Deposit
        4. Change Pin
        5. Exit
        
        =================================
        
        Choose an Option:  """))
        
        if(user_input == 1):
            self.check_balance()
        elif(user_input == 2):
            self.withdraw()
        elif(user_input == 3):
            self.deposit()
        elif(user_input == 4):
            self.change_pin()
        elif(user_input == 5):
            self.exit()
        else:
            print("Invalid Input")

    #check balance
    def check_balance(self): 
        print("Checking Balance...\n")
        i = 0
        while(i < 3):
            pin = int(input("Enter Your Pin: "))
            if(pin == self.pin):
                print("Checking...")
                print("Your Current Balance is: ", self.balance)
                break
            else:
                i += 1
                print("Incorrect Pin")
                print("Remaining Attempts: ", 3 - i ,"\n")
            if(i == 3):
                print("Too Many Wrong Attempts, Try Again Later")
                self.exit()
            print("=================================\n")

    #withdraw money
    def withdraw(self):
        print("Withdrawing Money...\n")
        i = 0
        while(i < 3):
            pin = int(input("Enter Your Pin: "))
            if(pin == self.pin):
                amount = int(input("Enter Amount to Withdraw: "))
                if(amount > self.balance):
                    print("Insufficient Balance")
                    break
                elif(amount <= 0):
                    print("Invalid Amount")
                    break
                else:
                    print("Withdrawing...")
                    print("Current Balance: ", self.balance)
                    self.balance -= amount
                    print("Amount Withdrawn: ", amount)
                    print("Remaining Balance: ", self.balance)
                    break
            else:
                i += 1
                print("Incorrect Pin")
                print("Remaining Attempts: ", 3 - i ,"\n")
            if(i == 3):
                print("Too Many Wrong Attempts, Try Again Later")
                self.exit()
            print("=================================\n")

    #deposit money
    def deposit(self): 
        print("Depositing Money...\n")
        i = 0
        while(i < 3):
            pin = int(input("Enter Your Pin: "))
            if(pin == self.pin):
                amount = int(input("Enter Amount to Deposit: "))
                print("Current Balance: ", self.balance)
                print("Depositing...")
                if(amount <= 0):
                    print("Invalid Amount")
                    break
                self.balance += amount
                print("Amount Deposited: ", amount)
                print("New Balance: ", self.balance)
                break
            else:
                i += 1
                print("Incorrect Pin")
                print("Remaining Attempts: ", 3 - i ,"\n")
            if(i == 3):
                print("Too Many Wrong Attempts, Try Again Later")
                self.exit()
            print("=================================\n")

    #change pin
    def change_pin(self): 
        print("Changing Pin...\n")
        i = 0
        while(i < 3):
            pin = int(input("Enter Your Current Pin: "))
            if(pin == self.pin):
                new_pin = int(input("Enter New Pin: "))
                self.pin = new_pin
                print("Pin Changed", self.pin)
                break
            else:
                i += 1
                print("Incorrect Pin")
                print("Remaining Attempts: ", 3 - i ,"\n")
            if(i == 3):
                print("Too Many Wrong Attempts, Try Again Later")
                self.exit()
            print("=================================\n")

    #exit
    def exit(self): 
        print("Exiting...\n")
        exit()

my_atm = ATM()