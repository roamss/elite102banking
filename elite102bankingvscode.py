from random import randint
    
class BankingSystem:
    def __init__(self):
        self.card_numbers = []
        self.pin_numbers = []
        self.iin = 400000
    
    def welcome(self):
        print(
            "1. Create an account\n"
            "2. Log into account\n"
            "0. Exit"
        )
        main_menu_selection = str(input())
        if main_menu_selection == "1":
            self.create_account()
        if main_menu_selection == "2":
            self.account_login()
        if main_menu_selection == "0":
            print("\n")
            return "Bye!"
    
    def create_account(self):
        credit_card_number = "400000" + format(randint(0000000000, 9999999999), '010d')
        pin_number = format(randint(0000, 9999), '04d')

        self.card_numbers.append(credit_card_number)
        self.pin_numbers.append(pin_number)

        print("\n")
        print("Your card has been created")
        print("Your card number:")
        print(credit_card_number)
        print("Your pin number:")
        print(pin_number)
        print("\n")
        self.welcome()

    def account_login(self):
        print("\n")
        print("Enter your card number:")
        entered_card_number = int(input())

        print("Enter your PIN:")
        entered_pin_number = int(input())

        if str(entered_card_number) in self.card_numbers and str(entered_pin_number) in self.pin_numbers:
            print("\n")
            print("You have successfully logged in!")
            self.acct_balance()
        else:
            print("\n")
            print("Wrong card number of PIN!")
            print("\n")
            self.welcome()

    def acct_balance(self):
        print(
            "\n1. Balance\n"
            "2. Log out\n"
            "0. Exit"
        )
        account_balance_selection = str(input())

        if account_balance_selection == "1":
            print("\n")
            print("Balance: 0")
            self.acct_balance()

        elif account_balance_selection == "2":
            print("\n")
            print("You have successfully logged out!")
            print("\n")
            self.welcome()

        elif account_balance_selection == "0":
            print("\n")
            print("Bye!")

print(BankingSystem().welcome())