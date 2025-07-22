# Bank application code# This code implements a simple banking application that allows users to create accounts, deposit, and withdraw money
# It uses a class to manage account details and operations.
# It also includes error handling for invalid inputs and insufficient funds.
# The code is structured to allow for easy expansion and modification in the future.
import random
class Bank:
    Holder_details=[]
    def create_new_Account(self):
        print('***======***Welcome To Union Bank***======***')
        new_holder={}

        new_holder['Holder_name'] = input("Enter Holder_name: ")
        new_holder['Mobile'] = input("Enter Mobile number: ")
        new_holder['Aadhar'] = input("Enter Aadhar number: ")
        new_holder['IFSCCODE'] = 'UBIN0800988'
        data= random.randint(1000000000000,9999999999999)
        new_holder['Account_number'] = data
        acc_type = input('Select Account Type Saving/ Zero:').lower()
        if acc_type == 'saving':
            while True:
                n1 = int(input('Enter minimum balance for saving account is ₹500 : '))  
                if n1 >= 500:
                    new_holder['Balance'] = n1
                    break
                else:
                    print('Deposit minimum ₹500')
        elif acc_type == 'zero':
            while True:
                n2 = int(input('Your account belongs to zero so deposit minimum ₹100: '))
                if n2 >= 100:
                    new_holder['Balance'] = n2
                    break
                else:
                    print('Deposit minimum ₹100')
        else:
            print("❌ Invalid account type.")
            return

        Bank.Holder_details.append(new_holder)
        print("✅ Account created! Your details:")
        print(new_holder)

    def deposit(self):
        print('======Welcome to Deposit======')
        name = input('Enter Holder_name: ')
        acc_num = int(input('Enter Account_number: '))
        amount = int(input('Enter deposit amount: '))
        for holder in Bank.Holder_details:
            if holder['Holder_name'] == name and holder['Account_number'] == acc_num:
                holder['Balance'] += amount
                print(f"✅ ₹{amount} deposited successfully. New Balance: ₹{holder['Balance']}")
                break
        else:
            print("❌ Account not found. Please check the details.")    
        print(Bank.Holder_details)

    def withdraw(self):
        print('======Welcome to Withdraw======')
        name = input('Enter Holder_name: ')
        acc_num = int(input('Enter Account_number: '))
        amount = int(input('Enter withdraw amount: '))
        for holder in Bank.Holder_details:
            if holder['Holder_name'] == name and holder['Account_number'] == acc_num:
                if holder['Balance'] >= amount:
                    holder['Balance'] -= amount
                    print(f"✅ ₹{amount} withdrawn successfully. New Balance: ₹{holder['Balance']}")
                    break
        else:
            print("❌ Insufficient balance.")
        
        print("❌ Account not found.")
        print(Bank.Holder_details)

obj=Bank()
while True:
    print('1. Create New Account\n'
        '2. Deposit\n'
        '3. Withdraw\n'
        '4. Exit')
    n1 = input('Enter your choice: ')
    if n1 == '1':
        obj.create_new_Account()
    elif n1 == '2':
        obj.deposit()
    elif n1 == '3':
        obj.withdraw()
    elif n1 == '4':
        print('🙏 Thank you for using Union Bank!')
        break
    else:
        print('❌ Invalid choice. Please try again.')






       
